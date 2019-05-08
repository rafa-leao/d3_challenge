def assets_from_path(path, js_found, css_found, img_found):

	assets_atached = [path, [], [], []]

	js_files  = []
	css_files = []
	img_files = []

	print("Cathing js files from {}".format(path))
	for js_file in js_found:
		# it is not going to catch javascript wrotten in the bare HTML file

		js_file = js_file.attrs["src"] if "src" in js_file.attrs else 'No file path :c'

		js_files.append(js_file)

	print("Cathing css files from {}".format(path))
	for css_file in css_found:
		# it is not going to catch css wrotten in the bare HTML file

		css_file = css_file.attrs["href"] if 'href' in css_file.attrs else 'No file path :c'

		css_files.append(css_file)

	print("Cathing img files from {}".format(path))
	for img_file in img_found:
		# it is not going to catch <link rel="icon"> yet

		img_file = img_file.attrs["src"] if "src" in img_file.attrs else 'No file path :c'

		img_files.append(img_file)

	assets_atached[1].append("JS_FILES: ")
	assets_atached[1].append(js_files)

	assets_atached[2].append("CSS_FILES: ")
	assets_atached[2].append(css_file)

	assets_atached[3].append("IMG_FILES: ")
	assets_atached[3].append(img_file)

	return assets_atached
