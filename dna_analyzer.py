"""
DNA Analyzer - Multi-format DNA raw data analysis
================================================

This module parses DNA files and compares them with the SNP database
to find interesting genetic traits.

Supported formats:
- 23andMe raw data (.txt)
- AncestryDNA raw data (.txt)
- MyHeritage DNA raw data (.csv)
- FamilyTreeDNA raw data
- LivingDNA raw data
"""

from snp_database import SNP_DATABASE, get_snp_info
import re


def detect_format(content):
    """
    Automatically detect the format of the DNA file.
    
    Returns:
        str: 'myheritage', '23andme', 'ancestry', 'ftdna', 'generic'
    """
    first_lines = content[:2000].lower()
    
    # MyHeritage CSV format (comma-separated with header)
    if 'rsid,chromosome,position,result' in first_lines or \
       '"rsid","chromosome","position","result"' in first_lines:
        return 'myheritage'
    
    # FamilyTreeDNA format
    if 'rsid,chromosome,position,result' in first_lines and 'familytreedna' in first_lines:
        return 'ftdna'
    
    # AncestryDNA format (has specific header)
    if 'ancestrydna' in first_lines:
        return 'ancestry'
    
    # 23andMe format (has specific comment header)
    if '23andme' in first_lines:
        return '23andme'
    
    # Check if it's CSV format (comma-separated)
    lines = content.strip().split('\n')[:10]
    comma_count = sum(1 for line in lines if ',' in line and line.count(',') >= 3)
    if comma_count > 5:
        return 'csv_generic'
    
    return 'generic'


def clean_value(value):
    """
    Clean quotes and whitespace from value.
    """
    if value is None:
        return ''
    # Remove quotes and whitespace
    return value.strip().strip('"').strip("'").strip()


def parse_csv_line(line):
    """
    Parse CSV line (preserving commas within quotes).
    """
    parts = []
    current = ''
    in_quotes = False
    quote_char = None
    
    for char in line:
        if char in ['"', "'"] and not in_quotes:
            in_quotes = True
            quote_char = char
        elif char == quote_char and in_quotes:
            in_quotes = False
            quote_char = None
        elif char == ',' and not in_quotes:
            parts.append(clean_value(current))
            current = ''
        else:
            current += char
    
    parts.append(clean_value(current))
    return parts


def parse_dna_file(content):
    """
    Parse multi-format DNA raw data file.
    
    Supported formats:
    - 23andMe: rsid\tchromosome\tposition\tgenotype
    - AncestryDNA: rsid\tchromosome\tposition\tallele1\tallele2
    - MyHeritage: RSID,CHROMOSOME,POSITION,RESULT (CSV)
    - FamilyTreeDNA: RSID,CHROMOSOME,POSITION,RESULT
    - Generic CSV/TSV
    
    Returns:
        dict: {rsid: {"chromosome": str, "position": int, "genotype": str}}
    """
    snps = {}
    
    # Detect format
    file_format = detect_format(content)
    
    # Process lines
    lines = content.split('\n')
    header_found = False
    column_map = None
    
    for line_num, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Skip comment lines
        if line.startswith('#'):
            continue
        
        # Header check for CSV formats
        if file_format in ['myheritage', 'csv_generic', 'ftdna']:
            # Detect header line
            line_lower = line.lower()
            if not header_found and ('rsid' in line_lower or 'snp' in line_lower):
                # This is the header line
                header_parts = parse_csv_line(line_lower)
                column_map = {}
                for i, col in enumerate(header_parts):
                    col = col.lower().strip()
                    if 'rsid' in col or col == 'snp' or col == 'snpid':
                        column_map['rsid'] = i
                    elif 'chrom' in col or col == 'chr':
                        column_map['chromosome'] = i
                    elif 'pos' in col:
                        column_map['position'] = i
                    elif 'result' in col or 'genotype' in col or 'allele' in col:
                        column_map['genotype'] = i
                
                header_found = True
                continue
            
            # Parse CSV line
            parts = parse_csv_line(line)
            
            if column_map and len(parts) >= len(column_map):
                try:
                    rsid = clean_value(parts[column_map.get('rsid', 0)]).lower()
                    chromosome = clean_value(parts[column_map.get('chromosome', 1)])
                    position = clean_value(parts[column_map.get('position', 2)])
                    genotype = clean_value(parts[column_map.get('genotype', 3)]).upper()
                    
                    # rsid check
                    if rsid.startswith('rs'):
                        # Convert position to integer
                        try:
                            pos_int = int(position) if position.isdigit() else 0
                        except:
                            pos_int = 0
                        
                        # Genotype cleaning
                        genotype = re.sub(r'[^ATCG]', '', genotype)
                        
                        if genotype and len(genotype) <= 2:
                            snps[rsid] = {
                                "chromosome": chromosome,
                                "position": pos_int,
                                "genotype": genotype
                            }
                except (IndexError, KeyError):
                    continue
        
        else:
            # 23andMe/AncestryDNA format (tab or space separated)
            if '\t' in line:
                parts = line.split('\t')
            else:
                parts = line.split()
            
            if len(parts) >= 4:
                rsid = parts[0].lower()
                
                # Only take SNPs starting with rs
                if rsid.startswith('rs'):
                    try:
                        chromosome = parts[1]
                        position = parts[2]
                        
                        # AncestryDNA format: allele1 and allele2 may be in separate columns
                        if len(parts) >= 5 and len(parts[3]) == 1 and len(parts[4]) == 1:
                            genotype = (parts[3] + parts[4]).upper()
                        else:
                            genotype = parts[3].upper()
                        
                        # Genotype cleaning
                        genotype = re.sub(r'[^ATCG]', '', genotype)
                        
                        # Convert position to integer
                        try:
                            pos_int = int(position) if position.isdigit() else 0
                        except:
                            pos_int = 0
                        
                        if genotype and len(genotype) <= 2:
                            snps[rsid] = {
                                "chromosome": chromosome,
                                "position": pos_int,
                                "genotype": genotype
                            }
                    except (ValueError, IndexError):
                        continue
    
    return snps


def normalize_genotype(genotype):
    """
    Normalize genotypes (for sorting).
    Example: "TA" -> "AT", "GA" -> "AG"
    """
    if len(genotype) == 2:
        return ''.join(sorted(genotype))
    return genotype


def check_genotype_match(user_genotype, variant_genotype):
    """
    Compare user's genotype with variant genotype in database.
    Check in both directions (AT == TA).
    """
    user_norm = normalize_genotype(user_genotype)
    variant_norm = normalize_genotype(variant_genotype)
    return user_norm == variant_norm


class DNAAnalyzer:
    """DNA analysis class"""
    
    def __init__(self, user_snps):
        """
        Args:
            user_snps: output of parse_dna_file()
        """
        self.user_snps = user_snps
        self.findings = []
    
    def analyze_snp(self, rsid):
        """
        Analyze a single SNP.
        
        Returns:
            dict or None: Result if finding exists, otherwise None
        """
        # Is this SNP in the database?
        snp_info = get_snp_info(rsid)
        if not snp_info:
            return None
        
        # Does the user have this SNP?
        user_data = self.user_snps.get(rsid.lower())
        if not user_data:
            return None
        
        user_genotype = user_data["genotype"]
        
        # Skip if genotype is "--" or "00" (no-call)
        if user_genotype in ["--", "00", "II", "DD", "DI", "ID"]:
            return None
        
        # Find variant match
        variants = snp_info.get("variants", {})
        matched_variant = None
        
        for variant_genotype, variant_info in variants.items():
            if check_genotype_match(user_genotype, variant_genotype):
                matched_variant = (variant_genotype, variant_info)
                break
        
        if not matched_variant:
            return None
        
        variant_genotype, variant_info = matched_variant
        
        # Create result
        return {
            "rsid": rsid,
            "gene": snp_info.get("gene", ""),
            "category": snp_info.get("category", ""),
            "title": snp_info.get("title", ""),
            "description": variant_info.get("description", ""),
            "effect": variant_info.get("effect", ""),
            "genotype": user_genotype,
            "frequency": snp_info.get("frequency", "")
        }
    
    def analyze_all(self):
        """
        Analyze all known SNPs.
        
        Returns:
            dict: {
                "total_snps": int,
                "analyzed_snps": int,
                "findings": list
            }
        """
        self.findings = []
        analyzed_count = 0
        
        for rsid in SNP_DATABASE.keys():
            result = self.analyze_snp(rsid)
            if result:
                self.findings.append(result)
                analyzed_count += 1
        
        # Sort by category
        category_order = [
            "extreme_rare", "rare", "interesting", "personality",
            "disease", "food", "fitness", "cognitive", "lifestyle"
        ]
        
        def sort_key(finding):
            cat = finding.get("category", "")
            try:
                return category_order.index(cat)
            except ValueError:
                return len(category_order)
        
        self.findings.sort(key=sort_key)
        
        return {
            "total_snps": len(self.user_snps),
            "analyzed_snps": analyzed_count,
            "findings": self.findings
        }
    
    def get_findings_by_category(self, category):
        """Get findings in a specific category"""
        return [f for f in self.findings if f.get("category") == category]
    
    def get_rare_findings(self):
        """Get rare findings"""
        rare_categories = ["extreme_rare", "rare"]
        return [f for f in self.findings if f.get("category") in rare_categories]
    
    def get_interesting_combinations(self):
        """
        Check for interesting gene combinations.
        Example: Red hair + blue eyes combination
        """
        combinations = []
        
        # Red hair + blue eyes combination
        red_hair_genes = ["rs1805007", "rs1805008"]
        blue_eye_genes = ["rs12913832"]
        
        has_red_hair = any(
            f for f in self.findings 
            if f.get("rsid") in red_hair_genes and f.get("effect") in ["positive", "carrier"]
        )
        
        has_blue_eyes = any(
            f for f in self.findings 
            if f.get("rsid") in blue_eye_genes and f.get("effect") in ["positive"]
        )
        
        if has_red_hair and has_blue_eyes:
            combinations.append({
                "rsid": "combo_red_blue",
                "gene": "MC1R + HERC2",
                "category": "interesting",
                "title": "Red Hair + Blue Eyes Combination",
                "description": "You have both red hair and blue eye genes! This combination is found in less than 1% of the world population.",
                "effect": "ultra_rare",
                "genotype": "Combination",
                "frequency": "<1% worldwide"
            })
        
        # Fast caffeine + morning person combination
        fast_caffeine = any(
            f for f in self.findings 
            if f.get("rsid") == "rs762551" and f.get("effect") == "fast"
        )
        
        morning_person = any(
            f for f in self.findings 
            if f.get("rsid") == "rs1801260" and f.get("effect") == "morning"
        )
        
        if fast_caffeine and morning_person:
            combinations.append({
                "rsid": "combo_morning_coffee",
                "gene": "CYP1A2 + CLOCK",
                "category": "interesting",
                "title": "Perfect Morning Coffee Genes",
                "description": "You have both fast caffeine metabolism and morning person genes! Morning coffee is ideal for you.",
                "effect": "synergy",
                "genotype": "Combination",
                "frequency": "~15%"
            })
        
        # Sprinter + power genes combination
        sprinter = any(
            f for f in self.findings 
            if f.get("rsid") == "rs1815739" and f.get("effect") == "power"
        )
        
        muscle_strength = any(
            f for f in self.findings 
            if f.get("rsid") == "rs1800169" and f.get("effect") in ["enhanced", "moderate"]
        )
        
        if sprinter and muscle_strength:
            combinations.append({
                "rsid": "combo_power_athlete",
                "gene": "ACTN3 + CNTF",
                "category": "interesting",
                "title": "Power Athlete Genes",
                "description": "You have both sprinter muscle type and increased muscle strength genes! You have a genetic advantage for explosive power sports.",
                "effect": "synergy",
                "genotype": "Combination",
                "frequency": "~8%"
            })
        
        # Strategist + high memory combination
        strategist = any(
            f for f in self.findings 
            if f.get("rsid") == "rs4680" and f.get("effect") == "worrier"
        )
        
        good_memory = any(
            f for f in self.findings 
            if f.get("rsid") == "rs9536314" and f.get("effect") in ["superior", "enhanced"]
        )
        
        if strategist and good_memory:
            combinations.append({
                "rsid": "combo_strategist",
                "gene": "COMT + KIBRA",
                "category": "interesting",
                "title": "Strategic Thinker Genes",
                "description": "You have both strategist (slow COMT) and strong memory genes! Ideal combination for analytical thinking and planning.",
                "effect": "synergy",
                "genotype": "Combination",
                "frequency": "~10%"
            })
        
        return combinations
    
    def get_full_report(self):
        """
        Create full analysis report.
        
        Returns:
            dict: All findings and statistics
        """
        # First do main analysis
        results = self.analyze_all()
        
        # Add interesting combinations
        combinations = self.get_interesting_combinations()
        
        # Add combinations to the beginning of findings
        all_findings = combinations + results["findings"]
        
        return {
            "total_snps": results["total_snps"],
            "analyzed_snps": results["analyzed_snps"] + len(combinations),
            "findings": all_findings
        }


# Main analysis function
def analyze_dna(content):
    """
    Analyze DNA file and return results.
    
    Args:
        content: DNA file content (string)
    
    Returns:
        dict: Analysis results
    """
    # Parse
    snps = parse_dna_file(content)
    
    # Analyze
    analyzer = DNAAnalyzer(snps)
    return analyzer.get_full_report()

