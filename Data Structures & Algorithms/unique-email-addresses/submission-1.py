class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        
        for email in emails:

            local_name, domain = email.split("@")

            local_name = local_name.replace(".", "")

            local_name_valid = local_name.split("+")[0]

            valid_email = local_name_valid+"@"+domain
            seen.add(valid_email)
            
        return len(seen)
