import os

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
    "about", "research", "teaching", 
    "publications", "photos", "misc",
  ]

  TEMPLATE = "content/template.html"


  ###################
  # Modify Template #
  ###################

  # Load template
  with open(TEMPLATE, "r") as file:
    template_html = file.read()
  # Convert list of pages into urls
  urls_html = "".join([make_link(
      page.capitalize(), 
      page + ".html", 
      padding = 4) + "\n" for page in PAGES])
  # Add the urls to the template
  template_html = template_html.replace("<!-- LINKS -->", urls_html)

  ################
  # Create Pages #
  ################

  PAGES = PAGES + ["index"]

  # Make all pages
  for page in PAGES:
    # Make content
    page_html = make_page(template_html, "content/{}.partial.html".format(page))
    # Write content
    with open("{}.html".format(page), "w") as file:
      file.write(page_html)

 

if __name__ == "__main__":
  main()
