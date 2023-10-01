import os

dimensionName = "1027"
dpiName = "77"
baseUrl = "https://edenferreira.github.io/fotografia/public"
baseUrlLocal = "./public"

def imageHtml(image, baseUrl, dimensionName, dpiName):
    just_name = os.path.splitext(image)[0]
    return f"""
  <figure>
    <a href="{baseUrl}/{image}">
      <img src="{baseUrl}/{just_name}_{dimensionName}_{dpiName}dpi.jpg"></img>
    </a>
  </figure>"""

def pageHtml(images, baseUrl, dimensionName, dpiName):
    imagesHtml = "\n".join([imageHtml(image, baseUrl, dimensionName, dpiName) for image in images])
    return f"""<html>

<head>
  <title>Eden Ferreira Fotografia</title>
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

if __name__ == "__main__":
    files = os.listdir(r"C:\Users\thiag\Meu Drive\Fotos Exportadas\Renovação Site")
    images = [f for f in files if not f.endswith("_" + dimensionName + "_" + dpiName + "dpi.jpg")]
    print(images)
    new_index = pageHtml(images, baseUrl, dimensionName, dpiName)
    print(new_index)
    with open("new_index.html", "w") as f:
        f.write(new_index)

    new_index_local = pageHtml(images, baseUrlLocal, dimensionName, dpiName)
    with open("new_index_local.html", "w") as f:
        f.write(new_index_local)
