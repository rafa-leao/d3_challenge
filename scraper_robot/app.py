from scraper.robot import Robot

if __name__ == '__main__':

    # This url is alredy with a allowed path. So the entry point to crawl on every page of this site is with this path!

    paths = Robot('https://scrapethissite.com/pages').paths_catcher()

    paths_found = []

    for path in paths:

        path_result = Robot('https://scrapethissite.com{}'.format(path)).paths_catcher()

        for single_path in path_result:

            if single_path.startswith('/'):

                paths_found.append(path)

    # remove duplicates
    print(list(dict.fromkeys(paths_found)))

    

