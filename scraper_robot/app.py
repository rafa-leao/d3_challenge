from scraper.robot import Robot

from utils.all_site_paths import all_site_paths

if __name__ == '__main__':

	print("Scraping...")

	# This url is alredy with a allowed path. So the entry point to crawl on every page of this site is with this path!
	paths = Robot().paths_catcher()

	print(paths)

	print(Robot().path_assets_catcher(paths))
