def assets_from_path(path, js_found, css_found, img_found):

	assets_atached = [path + "=>"]

	print("Cathing js files from {}".format(path))
	for js_file in js_found:
		# it is not going to catch javascript wrotten in the bare HTML file

		js_file = js_file.attrs["src"] if "src" in js_file.attrs else 'No file path :c'

		assets_atached.append("JS_FILE:")
		assets_atached.append(js_file)

	print("Cathing css files from {}".format(path))
	for css_file in css_found:
		# it is not going to catch css wrotten in the bare HTML file

		css_file = css_file.attrs["href"] if 'rel="stylesheet"' in css_file.attrs else 'No file path :c'

		assets_atached.append("CSS_FILE:")
		assets_atached.append(css_file)

	print("Cathing img files from {}".format(path))
	for img_file in img_found:
		# it is not going to catch <link rel="icon"> yet

		img_file = img_file.attrs["src"] if "src" in img_file.attrs else 'No file path :c'

		assets_atached.append("IMG_FILE:")
		assets_atached.append(img_file)

	return assets_atached
