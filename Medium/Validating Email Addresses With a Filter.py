# had to find a way to define username, websitename and extension variables. needed help from other coders online.
# once defined, everything else was quite straightforward

def fun(s):
    try:
        username, url = s.split('@')
        websitename, extension = url.split('.')
    except ValueError:
        return False
    if username.replace('-','').replace('_','').isalnum() is False:
        return False
    if websitename.isalnum() is False:
        return False
    if extension.isalpha() is False:
        return False
    if len(extension) > 3:
        return False
    else:
        return True
        
#end solution

#following is code from HackerRank to test code validity
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
