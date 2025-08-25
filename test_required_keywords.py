#!/usr/bin/env python3
"""
Test script to demonstrate the required keywords filtering functionality.
This script shows how the bot will filter job descriptions based on required keywords.
"""

def test_required_keywords_filter():
    """
    Test function to demonstrate how the required keywords filtering works.
    """
    # Import the required keywords from config
    from config.search import required_keywords
    
    print("=== Required Keywords Filter Test ===")
    print(f"Configured required keywords: {required_keywords}")
    print("Note: ALL keywords must be present in job description (AND condition)")
    print()
    
    # Sample job descriptions for testing
    test_jobs = [
        {
            "title": "Software Engineer - Visa Sponsorship Available",
            "description": "We are looking for a Software Engineer. We offer visa sponsorship and relocation assistance for expat candidates.",
            "should_pass": True
        },
        {
            "title": "Senior Developer - No Sponsorship",
            "description": "Senior developer position. Must be local candidate. No visa sponsorship or relocation assistance provided.",
            "should_pass": False
        },
        {
            "title": "Data Scientist - Partial Benefits",
            "description": "Data scientist role with visa sponsorship and relocation assistance. Great opportunity for expat professionals.",
            "should_pass": True
        },
        {
            "title": "Frontend Developer",
            "description": "Frontend developer position. We provide relocation assistance and welcome expat candidates.",
            "should_pass": False  # Missing "visa sponsorship"
        }
    ]
    
    def check_required_keywords(job_description: str, required_keywords: list) -> tuple[bool, list]:
        """
        Check if all required keywords are present in the job description.
        
        Args:
            job_description: The job description text
            required_keywords: List of keywords that must be present
            
        Returns:
            Tuple of (passes_filter, missing_keywords)
        """
        if not required_keywords:
            return True, []
            
        job_desc_lower = job_description.lower()
        missing_keywords = []
        
        for keyword in required_keywords:
            if keyword.lower() not in job_desc_lower:
                missing_keywords.append(keyword)
        
        return len(missing_keywords) == 0, missing_keywords
    
    # Test each job description
    for i, job in enumerate(test_jobs, 1):
        print(f"Test {i}: {job['title']}")
        print(f"Description: {job['description']}")
        
        passes, missing = check_required_keywords(job['description'], required_keywords)
        
        if passes:
            print("PASSES - All required keywords found")
        else:
            print(f"FAILS - Missing keywords: {', '.join(missing)}")
        
        expected = "EXPECTED" if job['should_pass'] else "EXPECTED"
        print(f"Result: {expected}")
        print("-" * 80)
    
    print("\n=== Configuration Instructions ===")
    print("To customize the required keywords filter:")
    print("1. Open 'config/search.py'")
    print("2. Find the 'required_keywords' variable")
    print("3. Modify the list to include your desired keywords")
    print("4. Set to empty list [] to disable this filter")
    print("\nExample configurations:")
    print("- For visa sponsorship jobs: ['visa sponsorship']")
    print("- For relocation assistance: ['relocation assistance']")
    print("- For expat positions: ['expat', 'visa sponsorship']")
    print("- For comprehensive filter: ['visa sponsorship', 'relocation assistance', 'expat']")

if __name__ == "__main__":
    test_required_keywords_filter()
