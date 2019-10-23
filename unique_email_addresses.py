class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        email_list = []
        
        for email in emails:
            local_name, domain_name = email.split('@')
            
            '''
            if '+' in local_name:
                index = local_name.index('+')
                local_name = local_name[:index]
            
            while '.' in local_name:
                index = local_name.index('.')
                local_name = local_name[:index] + local_name[index+1:]'''
            
            # The above two steps can be replaced by an one-line solution as below
            local_name = local_name.split('+')[0].replace('.', '')
            
            valid_email = local_name + '@' + domain_name
            email_list.append(valid_email)
        
        return len(set(email_list))