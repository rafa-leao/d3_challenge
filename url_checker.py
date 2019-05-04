from urllib.parse import urlparse

def url_checker(url_site,
                url_site_disallowed_path):

    validator = False

    for site_path in url_site_disallowed_path:

        """
            For now, this verification seems silly. 
            However, in the future, this software could receive the site url dynamically. 
            If so, this robot goes to the path "robots.txt" and see which paths are disallowed!
        """

        if site_path not in urlparse(url_site).path:

            validator = True
            continue

        else:

            validator= False
            break

    return validator
