import os

baseUrl = "https://edenferreira.github.io/fotografia/public"
baseUrlLocal = "./public"

def year_month_from_manifest(manifest):
    year, month = manifest.replace(".manifest", "").split("_")
    return [year, month]

def imageHtml(image_name, baseUrl):
    fhd_name = image_name.replace("RES", "FHD")
    fourK_name = image_name.replace("RES", "4K")
    return f"""
  <figure>
    <a href="{baseUrl}/{fourK_name}">
      <img src="{baseUrl}/{fhd_name}"></img>
    </a>
  </figure>"""

def pageHtml(title, images_names, baseUrl):
    imagesHtml = "\n".join([imageHtml(image_name, baseUrl) for image_name in images_names])
    return f"""<html>

<head>
  <title>{title}</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Quicksand">
  <link rel="stylesheet" href="normalize.css">
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://edenferreira.github.io/fotografia/normalize.css">
  <link rel="stylesheet" href="https://edenferreira.github.io/fotografia/styles.css">
</head>

<body>
{imagesHtml}

</body>

</html>
"""

def generate_one_page(title, images_names, manifest, page_name, baseUrl):
    year, month = year_month_from_manifest(manifest)
    new_index = pageHtml(title, images_names, f"{baseUrl}/{year}/{month}")
    with open(f"{page_name}.html", "w") as f:
        f.write(new_index)

# TODO dependency inversion for the withName thing

def imageHtmlWithName(image_name, baseUrl):
    fhd_name = image_name.replace("RES", "FHD")
    fourK_name = image_name.replace("RES", "4K")
    return f"""
  <figure>
    <a href="{baseUrl}/{fourK_name}">
      <img src="{baseUrl}/{fhd_name}"></img>
    </a>
    <p>{fourK_name}</p>
  </figure>"""

def pageHtmlWithName(title, images_names, baseUrl):
    imagesHtml = "\n".join([imageHtmlWithName(image_name, baseUrl) for image_name in images_names])
    return f"""<html>

<head>
  <title>{title}</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Quicksand">
  <link rel="stylesheet" href="normalize.css">
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://edenferreira.github.io/fotografia/normalize.css">
  <link rel="stylesheet" href="https://edenferreira.github.io/fotografia/styles.css">
</head>

<body>
{imagesHtml}

</body>

</html>
"""

def generate_one_page_with_name(title, images_names, manifest, page_name, baseUrl):
    year, month = year_month_from_manifest(manifest)
    new_index = pageHtmlWithName(title, images_names, f"{baseUrl}/{year}/{month}")
    with open(f"{page_name}_with_name.html", "w") as f:
        f.write(new_index)


if __name__ == "__main__":
    most_recent_year, most_recent_month = ["2024", "janeiro"]
    manifests = [f for f in os.listdir(f".\\public") if f.endswith(".manifest")]
    manifest = "2024_janeiro.manifest"
    year, month = manifest.replace(".manifest", "").split("_")
    title = "Eden Ferreira Fotografia"
    for manifest in manifests:
        images_names = None
        year, month = year_month_from_manifest(manifest)
        with open(f".\\public\\{manifest}", "r") as f:
            images_names = list(f.readlines())
        generate_one_page(f"{month} {year}", images_names, manifest, f"{year}_{month}_local", baseUrlLocal)
        generate_one_page(f"{month} {year}", images_names, manifest, f"{year}_{month}", baseUrl)
        generate_one_page_with_name(f"{month} {year}", images_names, manifest, f"{year}_{month}", baseUrl)
        if year == most_recent_year and month == most_recent_month:
            generate_one_page(title, images_names, manifest, "new_index_local", baseUrlLocal)
            generate_one_page(title, images_names, manifest, "new_index", baseUrl)
            generate_one_page_with_name(title, images_names, manifest, "new_index", baseUrl)
