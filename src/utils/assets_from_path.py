def assets_from_path(path, js_found, css_found, img_found):

	assets_files = {
		'path:': path,
		'JS_FILES': [],
		'CSS_FILES': [],
		'IMG_FILES': []
	}

	print("Cathing js files from {}".format(path))
	for js_file in js_found:
		# it is not going to catch javascript wrotten in the bare HTML file

		js_file = js_file.attrs["src"] if "src" in js_file.attrs else 'No file path :c'

		assets_files['JS_FILES'].append(js_file)

	print("Cathing css files from {}".format(path))
	for css_file in css_found:
		# it is not going to catch css wrotten in the bare HTML file

		css_file = css_file.attrs["href"] if 'href' in css_file.attrs else 'No file path :c'

		assets_files['CSS_FILES'].append(css_file)

	print("Cathing img files from {}".format(path))
	for img_file in img_found:
		# it is not going to catch <link rel="icon"> yet

		img_file = img_file.attrs["src"] if "src" in img_file.attrs else 'No file path :c'

		assets_files['IMG_FILES'].append(img_file)

	print("-*-------------*-------------*-------------*-------------*-------------*-")

	return assets_files
