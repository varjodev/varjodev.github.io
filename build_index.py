import json
import webbrowser

def embed_media(project_data):
    s = ""
    if project_data["media_type"] == "video":
        s += "<div class='ratio ratio-1x1'>"
        s += f"<iframe src='{project_data['media_source']}' allowfullscreen></iframe>"
        s += "</div>"
        
    elif project_data["media_type"] == "image":
        s += f"<img src='{project_data['media_source']}' class='img-fluid'>"

    elif project_data["media_type"] == "code":
        s += "<div class='container border bg-dark text-white p-3'>"
        s += project_data["media_source"]
        s += "</div>"

    s += f"<p>{project_data['media_caption']}</p>"

    return s

def generate_tags(tags):
    s = "<p class='tags'>"
    for tag in tags:
        s += f"<span class='badge rounded-pill bg-secondary mx-1'>{tag.capitalize()}</span>"
    s += "</p>"
    return s

def generate_main_project(project_data):
    s = "<div class='row-fluid m-3 project'>"
    s += "<div class='row project-title'>"
    s += f"<h3>{project_data['title']}</h3>"
    s += generate_tags(project_data["tags"])
    s += "</div>"
    s += "<div class='row'>"
    s += "<div class='col-5' style='word-wrap:break-word';><div class='container mt-auto'>"
    s += f"<p class='text-secondary'><small>{project_data['subtitle']}</small></p>"
    s += "</div>"
    s += f"<p>{project_data['description']}</p>"
    s += "<div class='container'>"
    if project_data["notes"] != "":
        s += f"<p class='text-secondary'><small> Notes: {project_data['notes']}</small></p>"
    s += f"<a href='{project_data['repo_link']}'> Link to repo </a>"
    s += "</div></div>"
    s += "<div class='col-1'></div>"

    # Media content
    s += "<div class='col-5'>"
    s += embed_media(project_data)
    s += "</div></div><hr/></div>"
    return s

def generate_misc_project(project_data):
    s = "<div class='col-5 project'>"
    s += "<div class='row project-title'>"
    s += f"<h5>{project_data['title']}</h5>"
    s += generate_tags(project_data["tags"])
    s += "</div>"
    s += f"<p>{project_data['description']}</p> </div>"
    return s

def generate_content_page():
    return "<div class='container my-3 p-3 rounded' style='background-color:rgb(255, 255, 255);'>"

def generate_filter_buttons():
    s = ""
    for i, tag in enumerate(['ALL', 'IMAGE', 'AUDIO', 'WEB', 'MICROCONTROLLERS']):
        btn_type = "primary" if i == 0 else "secondary"
        s += f'<button type="button" class="btn btn-{btn_type} mx-1 filter-btn" value="{tag}" onclick="projectFilter('
        s += f"'{tag}')"
        s += f'">{tag.capitalize()}</button>'
    return s

def generate_navbar():
    s = ""
    s += "<nav class='navbar navbar-expand-sm bg-dark navbar-dark fixed-top'>"
    s += "<div class='container-fluid'><a class='navbar-brand' href='https://github.com/varjodev/varjodev.github.io'>Projects page</a><ul class='navbar-nav'>"
    s += generate_filter_buttons()
    s += "</ul></div></nav>"
    return s

def html_prettify(s):
    pass

with open('content.json', 'r', encoding='utf-8') as file:
    content = json.load(file)

# Start document and head
html = ""
html += "<!DOCTYPE html><html lang='en'>"
html += "<head><meta charset='utf-8'><title>Varjo projects</title><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH' crossorigin='anonymous'></head>"

# Start body and main title/navbar
html += "<body style='background-color:rgb(228, 228, 228);'>"
# html += "<div class='container mt-3 p-3 rounded' style='background-color:rgb(255, 255, 255);'>"
# html += "<div class='row'>"
# html += "<h1>Projects page</h1></div>"

# # Generate filter tag buttons
# for tag in ['ALL', 'IMAGE', 'AUDIO', 'WEB']:
#     html += f'<button type="button" class="btn btn-primary mx-1 tag" onclick="projectFilter('
#     html += f"'{tag}')"
#     html += f'">{tag.capitalize()}</button>'
# html += "</div>"

html += generate_navbar()

html += "<div class='container my-4'>&nbsp;</div>"

# Generate main projects
html += generate_content_page()
for project_name in content["main_projects"]:
    html += generate_main_project(content["main_projects"][project_name])
html += "</div>"


# Generate misc projects
html += generate_content_page()
html += "<div class='row-fluid m-3'><div class='row mb-3'>"
html += "<h3> Other projects and work </h3>"
html += "<p>(more details can be provided on request)</p></div>"

for i, project_name in enumerate(content["misc_projects"]):
    if i % 2 == 0:
        html += "<div class='row mb-3'>"
        html += generate_misc_project(content["misc_projects"][project_name])
        html += "<div class='col-1'></div>"
        
    else:
        html += generate_misc_project(content["misc_projects"][project_name])
        html += "</div>"
        html += "<hr/>"
        

if i % 2 == 0:
    html += "</div>"

html += "</div>"
html += "</div>"

# TODO: Add misc gallery
html += generate_content_page()
html += "<div class='row-fluid m-3'><div class='row mb-3'>"
html += "<h3> Misc gallery </h3>"
html += "</div>"
for i, project_data in enumerate(content["media_gallery"]):
    if i % 2 == 0:
        html += "<div class='row mb-3'>"
        html += "<div class='col-5'>"
        html += embed_media(project_data)
        html += "</div>"
        html += "<div class='col-1'></div>"
        
    else:
        html += "<div class='col-5'>"
        html += embed_media(project_data)
        html += "</div>"
        html += "<hr/>"

if i % 2 == 0:
    html += "</div>"

html += "</div>"
html += "</div>"

# Bootstrap script
html += "<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz' crossorigin='anonymous'></script>"

# Tag filtering javascript
html += "\n\n"
html += """<script>
            function projectFilter(filter_tag) {
                var x, i, j, tags, tag_found;
                x = document.getElementsByClassName("project");
                for (i = 0; i < x.length; i++){
                    tag_found = 0;
                    if (filter_tag=="ALL"){
                    tag_found = 1;
                    }
                    // console.log(x[i].getElementsByClassName("project-title")[0]);
                    tags = x[i].getElementsByClassName("project-title")[0].getElementsByClassName("tags")[0].getElementsByClassName("badge");
                    for (j=0; j < tags.length; j++){
                        if (tags[j].textContent.toUpperCase() == filter_tag){
                        tag_found = 1;}
                    }
                    if (tag_found == 1) {
                        x[i].classList.remove("d-none");
                    }
                    else {
                        x[i].classList.add("d-none");
                    }
                }
                btns = document.getElementsByClassName("filter-btn");
                for (i = 0; i < btns.length; i++){
                    if (btns[i].value == filter_tag){
                    btns[i].classList.remove("btn-secondary");
                    btns[i].classList.add("btn-primary");
                    }
                    else{
                        btns[i].classList.remove("btn-primary");
                        btns[i].classList.add("btn-secondary");
                    }
                }
            }
            </script>"""

# Close body and html
html += "</body></html>"

# Write to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Open the html with default browser
webbrowser.open("index.html")