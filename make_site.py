import os
import pandas as pd

def make_link(label, url, padding=0):
  pads = " "*padding
  link_html = pads + "<a href='{}'>{}</a>".format(url, label)
  return link_html

def make_page(template_html, content_url, replace_str="<!-- CONTENT -->"):
  # Init page from template
  page_html = template_html

  try:
    # Open page's content
    with open(content_url) as file:
      content_html = file.read()

    # Add content to template
    page_html = page_html.replace(replace_str, content_html)
  except:
    print("No file `{}`: created empty page.".format(content_url))
    page_html = page_html.replace(replace_str, "")

  return page_html


def main():

  ###############
  # DEFINITIONS #
  ###############

  PAGES = [
    ("about"        , None),
    ("research"     , None),
    ("publications" , "https://scholar.google.com/citations?user=jLuwYGAAAAAJ&hl"),
    ("photos"       , None),
    ("misc"         , None),
  ]

  TEMPLATE = "content/template.html"

  PHOTO_ALBUMS_FILE = "content/photo_directory.csv"

  ###################
  # Modify Template #
  ###################

  # Load template
  with open(TEMPLATE, "r") as file:
    template_html = file.read()
  # Convert list of pages into urls

  urls_html = ""
  for page in PAGES:
    # Generate url from page name
    if page[1] is None:
      url  = page[0] + ".html"
    # Use external url
    else:
      url = page[1]
    # Create HTML link
    urls_html += make_link(page[0].capitalize(), url, padding = 4)

  # Add the urls to the template
  template_html = template_html.replace("<!-- LINKS -->", urls_html)

  ################
  # Create Pages #
  ################

  # Make Index page
  page_html = make_page(template_html, "content/{}.partial.html".format("index"))
  # Write content
  with open("index.html", "w") as file:
    file.write(page_html)

  # Make About page
  page_html = make_page(template_html, "content/{}.partial.html".format("about"))
  # Write content
  with open("about.html", "w") as file:
    file.write(page_html)

  # Make Research page
  page_html = make_page(template_html, "content/{}.partial.html".format("research"))
  # Write content
  with open("research.html", "w") as file:
    file.write(page_html)

  # Make Misc page
  page_html = make_page(template_html, "content/{}.partial.html".format("misc"))
  # Write content
  with open("misc.html", "w") as file:
    file.write(page_html)

  #######################
  # Create Photo Albums #
  #######################

  # Load photo albums
  dfPhoto = pd.read_csv(PHOTO_ALBUMS_FILE)
  dfPhoto.fillna('', inplace=True)

  # Different album categories -> each a unique page
  categories = dfPhoto["Category"].unique()
  navlinks = "".join(['<div class="photo_nav_col"><a href="{}">{}</a></div>'.format("photos_" + cat + ".html", cat) for cat in categories])

  # Create photos page
  page = "photos"
  page_html = make_page(template_html, "content/{}.partial.html".format(page))
  # Create nav links
  page_html = page_html.replace("<!-- ALBUM_NAV -->", navlinks)
  # Write content
  with open("{}.html".format(page), "w") as file:
      file.write(page_html)

  # Make each album page
  for cat in categories:

      page = "photos_{}".format(cat)

      # Subset directory
      dfCat = dfPhoto[dfPhoto["Category"] == cat]

      # Init page
      page_html = make_page(template_html, "content/photos_pages.partial.html")

      # Populate HTML nav links
      page_html = page_html.replace("<!-- ALBUM_NAV -->", navlinks)

      # Populate highlights
      # Get rows where thumbnail is provided
      dfHighlights = dfCat[dfCat["Thumbnail"] != ""]

      hrows = list(zip(dfHighlights["Date"],
                       dfHighlights["Album"],
                       dfHighlights["Link"],
                       dfHighlights["Thumbnail"]))

      # A max of 4 highlights (uses first 4 found)
      hrows = hrows[:4]

      div_i = 2
      highlights_html = ""
      for hrow in hrows:
        highlights_html += \
              '<div class="div{}p"> <a href={}> <img id="photo" src="{}"</img> </a> <p id="photodate"> {} </p> <p id="photodesc"> {} </p></div>'.format(str(div_i), hrow[2], hrow[3], hrow[0], hrow[1])
        div_i += 1


      page_html = page_html.replace("<!-- HIGHLIGHTS -->", highlights_html)



      # Populate HTML albums table
      rows = zip(dfCat["Trip"],
                 dfCat["Date"],
                 dfCat["Album"],
                 dfCat["Link"])
      albums_html = \
              "".join(['<tr> <td class="tg-0lax">{}</td>  <td class="tg-0lax">{}</td> <td class="tg-0lax"><a href="{}">{}</a></td> </tr>'.format(
            row[0], row[1], row[3], row[2]) for row in rows])

      page_html = page_html.replace("<!-- ALBUM_TABLE -->", albums_html)


      # Write content
      with open("{}.html".format(page), "w") as file:
          file.write(page_html)



if __name__ == "__main__":
  main()
