from urllib.parse import urlparse


def url_checker(url_site,
                url_site_disallowed_path):

    validator = False

    for site_path in url_site_disallowed_path:

        if site_path not in urlparse(url_site).path:

            validator = True
            continue

        else:

            validator = False
            break

    return validator
