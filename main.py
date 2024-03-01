import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import Label
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import END
import math
import os
folder_path = "ideologies"
ideologies = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
folder_path2 = "factions"
factions = [f for f in os.listdir(folder_path2) if os.path.isfile(os.path.join(folder_path2, f))]
folder_path3 = "headers"
headers = [f for f in os.listdir(folder_path3) if os.path.isfile(os.path.join(folder_path3, f))]
folder_path4 = "flags"
flags = [f for f in os.listdir(folder_path4) if os.path.isfile(os.path.join(folder_path4, f))]
folder_path5 = "focus_icons"
focuses = [f for f in os.listdir(folder_path5) if os.path.isfile(os.path.join(folder_path5, f))]
folder_path6 = "leaders"
leaders = [f for f in os.listdir(folder_path6) if os.path.isfile(os.path.join(folder_path6, f))]
folder_path7 = "news_image"
news_image = [f for f in os.listdir(folder_path7) if os.path.isfile(os.path.join(folder_path7, f))]
folder_path8 = "super_image"
superevent_image = [f for f in os.listdir(folder_path8) if os.path.isfile(os.path.join(folder_path8, f))]
def draw_text_psd_style(draw, xy, text, font, tracking=0, leading=None, **kwargs):
    """
    usage: draw_text_psd_style(draw, (0, 0), "Test",
                tracking=-0.1, leading=32, fill="Blue")

    Leading is measured from the baseline of one line of text to the
    baseline of the line above it. Baseline is the invisible line on which most
    letters—that is, those without descenders—sit. The default auto-leading
    option sets the leading at 120% of the type size (for example, 12‑point
    leading for 10‑point type).

    Tracking is measured in 1/1000 em, a unit of measure that is relative to
    the current type size. In a 6 point font, 1 em equals 6 points;
    in a 10 point font, 1 em equals 10 points. Tracking
    is strictly proportional to the current type size.
    """

    def stutter_chunk(lst, size, overlap=0, default=None):
        for i in range(0, len(lst), size - overlap):
            r = list(lst[i:i + size])
            while len(r) < size:
                r.append(default)
            yield r

    x, y = xy
    font_size = font.size
    lines = text.splitlines()
    if leading is None:
        leading = font.size * 1.2
    for line in lines:
        for a, b in stutter_chunk(line, 2, 1, ' '):
            w = font.getlength(a + b) - font.getlength(b)
            
            print("[debug] kwargs:{}".format(kwargs))

            draw.text((x, y), a, font=font, **kwargs)
            x += w + (tracking / 1000) * font_size
        y += leading
        x = xy[0]


pozycja1 = (355, 13)
pozycja2 = (355, 43)
pozycja3 = (355, 71)
pozycja4 = (391, 155)
kolor_tekstu = (255, 255, 255)
kolor_tekstu2 = (176, 186, 189)
kolor_tekstu3 = (38, 30, 16)
kolor_tekstu4 = (185, 195, 199)
pozycja6 = (391, 191)
pozycja7 = (391, 232)
pozycja9 = (37, 14)
pozycja12 = (239, 139)
pozycja16 = (470, 545)
pozycja17 = (439, 985)
pozycja18 = (265, 539)
pozycja21 = (876, 190)


def add_text_to_img():
    tekst = country_entry.get()
    kraj = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(kraj)
    font = ImageFont.truetype('BOMBARD_.ttf', 28)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-65, font=font, fill=kolor_tekstu, leading=None)
    global wynikowy_obraz
    wynikowy_obraz = kraj


def add_text_to_img2():
    tekst = faction_entry.get()
    if tekst == '':
        tekst = "No faction"
    frakcja = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frakcja)
    font = ImageFont.truetype('BOMBARD_.ttf', 28)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-65, font=font, fill=kolor_tekstu, leading=None)
    global wynikowy_obraz2
    wynikowy_obraz2 = frakcja


def factions_choose():
    selected2 = selected_option2.get()
    global wynikowy_obraz13
    wynikowy_obraz13 = selected2


def add_text_to_img3():
    tekst = leader_entry.get()
    if tekst == '':
        tekst = "No leader"
    leader = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(leader)
    font = ImageFont.truetype('BOMBARD_.ttf', 28)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-65, font=font, fill=kolor_tekstu, leading=None)
    global wynikowy_obraz3
    wynikowy_obraz3 = leader


def add_text_to_img4():
    tekst = party_entry.get()
    party = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(party)
    font = ImageFont.truetype('Aldrich-Regular.ttf', 29)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-25, font=font, fill=kolor_tekstu2, leading=None)
    global wynikowy_obraz4
    wynikowy_obraz4 = party


def ideologies_choose():
    selected = selected_option.get()
    global wynikowy_obraz5
    wynikowy_obraz5 = selected


def add_text_to_img6():
    tekst = ideologia_entry.get()
    ideologia = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(ideologia)
    font = ImageFont.truetype('Aldrich-Regular.ttf', 27)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-75, font=font, fill=kolor_tekstu2, leading=None)
    global wynikowy_obraz6
    wynikowy_obraz6 = ideologia


def add_text_to_img7():
    tekst = "Next election: " + wybory_entry.get()
    if tekst == 'Next election: ':
        tekst = "Next election: Never"
    wybory = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(wybory)
    font = ImageFont.truetype('Aldrich-Regular.ttf', 25)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-25, font=font, fill=kolor_tekstu2, leading=None)
    global wynikowy_obraz7
    wynikowy_obraz7 = wybory


def add_text_to_img8():
    tekst = focus_entry.get()
    if tekst == '':
        tekst = "Select a National Focus"
    focus = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(focus)
    font = ImageFont.truetype('Aldrich-Regular.ttf', 31)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-50, font=font, fill=kolor_tekstu2, leading=None)
    global wynikowy_obraz8
    wynikowy_obraz8 = focus


def browse_flag():
    file_path = 'flags/' + selected_option_flag.get()
    if file_path:
        image = Image.open(file_path).convert("RGBA")
        image = image.resize((146, 90))
        global wynikowy_obraz9
        wynikowy_obraz9 = image


def browse_focus():
    file_pathf = 'focus_icons/' + selected_option_focus.get()
    if file_pathf:
        imagef = Image.open(file_pathf).convert("RGBA")
        imagef = imagef.crop(imagef.getbbox())
        if imagef.size[0] / imagef.size[1] >= 1:
            imagef = imagef.resize((152, int(math.ceil(152 / imagef.size[0] * imagef.size[1]))))
        else:
            imagef = imagef.resize((int(math.ceil(128 / imagef.size[1] * imagef.size[0])), 128))
        global wynikowy_obraz10
        wynikowy_obraz10 = imagef


def browse_leader():
    file_pathl = 'leaders/' + selected_option_leader.get()
    if file_pathl:
        imagel = Image.open(file_pathl).convert("RGBA")
        imagel = imagel.crop(imagel.getbbox())
        
        if imagel.size[0] / imagel.size[1] >= 1:
            imagel = imagel.resize((192, int(math.ceil(192 / imagel.size[0] * imagel.size[1]))))
        else:
            imagel = imagel.resize((int(math.ceil(258 / imagel.size[1] * imagel.size[0])), 258))

        global wynikowy_obraz11
        wynikowy_obraz11 = imagel


def generate_pie_chart(size=(105, 105)):
    data = [int(id_en_entry.get()), int(id_ns_entry.get()), int(id_f_entry.get()), int(id_un_entry.get()), int(id_d_entry.get()), int(id_p_entry.get()), int(id_c_entry.get()), int(id_lc_entry.get()), int(id_lib_entry.get()), int(id_pr_entry.get()), int(id_s_entry.get()), int(id_co_entry.get())]
    data.reverse()
    total = sum(data)
    colours = [(52, 25, 80), (80, 50, 0), (132, 50, 0), (35, 35, 35), (75, 75, 75), (130, 130, 130), (0, 0, 135), (39, 49, 149), (78, 97, 163), (169, 27, 79), (155, 0, 0), (110, 0, 1)]
    colours.reverse()
    start_angle = 0
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    i = 0
    for value in data:
        angle = 360 * value / total
        draw.pieslice((0, 0, size[0], size[1]), start_angle, start_angle + angle, fill=colours[i])
        start_angle += angle
        i = i + 1
    global wynikowy_obraz12
    wynikowy_obraz12 = img


def header_choose():
    selected3 = selected_option3.get()
    global wynikowy_obraz14
    wynikowy_obraz14 = selected3


def add_text_to_img15():
    tekst = title_entry.get()
    title = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(title)
    font = ImageFont.truetype('OldTyperNr.ttf', 24)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=20, font=font, fill=kolor_tekstu3, leading=None)
    global wynikowy_obraz15
    wynikowy_obraz15 = title


def add_text_to_img16():
    tekst = gazeta_entry.get(1.0, END)
    gazeta = Image.new('RGBA', (400, 425), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gazeta)
    font = ImageFont.truetype('OldTyperNr.ttf', 19)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-50, font=font, fill=kolor_tekstu3, leading=None)
    global wynikowy_obraz16
    wynikowy_obraz16 = gazeta


def browse_news_img():
    file_path_news = 'news_image/' + selected_option_news.get()
    if file_path_news:
        imagel = Image.open(file_path_news).convert("RGBA")
        imagel = imagel.crop(imagel.getbbox())
        imagel = imagel.resize((int(math.ceil(509 / imagel.size[1] * imagel.size[0])), 509))
        imagel = imagel.crop((0,0,201,509))
        global wynikowy_obraz18
        wynikowy_obraz18 = imagel


def add_text_to_img19():
    tekst = button_news_entry.get()
    title = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(title)
    font = ImageFont.truetype('OldTyperNr.ttf', 20)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-50, font=font, fill=kolor_tekstu3, leading=None)
    global wynikowy_obraz19
    wynikowy_obraz19 = title


def add_text_to_img20():
    tekst = title_sup_entry.get()
    title = Image.new('RGBA', (600, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(title)
    font = ImageFont.truetype('Aldrich-Regular.ttf', 37)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-5, font=font, fill=kolor_tekstu4, leading=None)
    global wynikowy_obraz20
    wynikowy_obraz20 = title


def browse_super_img():
    file_path_super = 'super_image/' + selected_option_super.get()
    if file_path_super:
        imagel = Image.open(file_path_super).convert("RGBA")
        imagel = imagel.crop(imagel.getbbox())
        
        if imagel.size[0]/imagel.size[1] >= 1032/704:
            imagel = imagel.resize((int(math.ceil(704 / imagel.size[1] * imagel.size[0])), 704))
        else:
            imagel = imagel.resize((1032, int(math.ceil(1032 / imagel.size[0] * imagel.size[1]))))
        imagel = imagel.crop((0, 0, 1032, 704))
        global wynikowy_obraz21
        wynikowy_obraz21 = imagel


def add_text_to_img21():
    tekst = button_sup_entry.get()
    title = Image.new('RGBA', (1000, 45), (0, 0, 0, 0))
    draw = ImageDraw.Draw(title)
    font = ImageFont.truetype('BOMBARD_.ttf', 46)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-65, font=font, fill=kolor_tekstu, leading=None)
    global wynikowy_obraz22
    wynikowy_obraz22 = title


def add_text_to_img22():
    tekst = quote_sup_entry.get()
    title = Image.new('RGBA', (1000, 45), (0, 0, 0, 0))
    draw = ImageDraw.Draw(title)
    font = ImageFont.truetype('BOMBARD_.ttf', 46)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-65, font=font, fill=kolor_tekstu, leading=None)
    global wynikowy_obraz23
    wynikowy_obraz23 = title


def add_text_to_img23():
    tekst = author_sup_entry.get()
    tekst = "-" + tekst
    title = Image.new('RGBA', (1000, 45), (0, 0, 0, 0))
    draw = ImageDraw.Draw(title)
    font = ImageFont.truetype('BOMBARD_.ttf', 46)
    draw_text_psd_style(draw, (0, 0), tekst, tracking=-65, font=font, fill=kolor_tekstu, leading=None)
    global wynikowy_obraz24
    wynikowy_obraz24 = title


def generate_final_image():
    if 'wynikowy_obraz' not in globals():
        result_label.config(text="Firstly add country name to image.")
    else:
        template_image = Image.open(r'template.png').convert("RGBA")
        final1 = wynikowy_obraz.resize((654, 36))
        template_image.alpha_composite(final1, dest=pozycja1)
        final2 = wynikowy_obraz2.resize((654, 36))
        template_image.alpha_composite(final2, dest=pozycja2)
        final3 = wynikowy_obraz3.resize((654, 36))
        template_image.alpha_composite(final3, dest=pozycja3)
        final4 = wynikowy_obraz4.resize((600, 36))
        template_image.alpha_composite(final4, dest=pozycja4)
        ideol = Image.open("ideologies/" + wynikowy_obraz5).convert("RGBA")
        mniej = int(ideol.width) / 2
        mniej2 = int(ideol.height) / 2
        print(mniej)
        print(mniej2)
        pozycja5 = (294 - math.ceil(mniej), 60 - math.ceil(mniej2))
        template_image.alpha_composite(ideol, dest=pozycja5)
        final6 = wynikowy_obraz6.resize((630, 36))
        template_image.alpha_composite(final6, dest=pozycja6)
        final7 = wynikowy_obraz7.resize((618, 36))
        template_image.alpha_composite(final7, dest=pozycja7)
        final8 = wynikowy_obraz8.resize((678, 36))
        final8o1 = final8.crop(final8.getbbox())
        mnieji = int(final8o1.width) / 2
        pozycja8 = (618 - math.ceil(mnieji), 301)
        template_image.alpha_composite(final8, dest=pozycja8)
        final9 = wynikowy_obraz9
        template_image.alpha_composite(final9, dest=pozycja9)
        overlay = Image.open("flag_overlay.png").convert("RGBA")
        template_image.alpha_composite(overlay, dest=pozycja9)
        final10 = wynikowy_obraz10
        mniejk = int(final10.width) / 2
        mniejk2 = int(final10.height) / 2
        pozycja10 = (294 - math.ceil(mniejk), 319 - math.ceil(mniejk2))
        template_image.alpha_composite(final10, dest=pozycja10)
        final11 = wynikowy_obraz11
        mniejl = int(final11.width) / 2
        pozycja11 = (109 - math.ceil(mniejl), 379 - final11.height)
        template_image.alpha_composite(final11, dest=pozycja11)
        underlay = Image.open("bck_shadow.png").convert("RGBA")
        template_image.alpha_composite(underlay, dest=(pozycja12[0] - 4, pozycja12[1] - 4))
        final12 = wynikowy_obraz12
        template_image.alpha_composite(final12, dest=pozycja12)
        overlay2 = Image.open("shadow.png").convert("RGBA")
        template_image.alpha_composite(overlay2, dest=pozycja12)
        ideolfact = Image.open("factions/" + wynikowy_obraz13).convert("RGBA")
        mniejfact = int(ideolfact.width) / 2
        mniejfact2 = int(ideolfact.height) / 2
        print(mniejfact)
        print(mniejfact2)
        pozycja13 = (793 - math.ceil(mniejfact), 64 - math.ceil(mniejfact2))
        template_image.alpha_composite(ideolfact, dest=pozycja13)
        ideolhead = Image.open("headers/" + wynikowy_obraz14).convert("RGBA")
        mniejhead = int(ideolhead.width) / 2
        mniejhead2 = int(ideolhead.height) / 2
        pozycja14 = (555 - math.ceil(mniejhead), 435 - math.ceil(mniejhead2))
        template_image.alpha_composite(ideolhead, dest=pozycja14)
        final15 = wynikowy_obraz15.resize((516, 36))
        final15o1 = final15.crop(final15.getbbox())
        mnojo = int(final15o1.width) / 2
        pozycja15 = (548 - math.ceil(mnojo), 506)
        template_image.alpha_composite(final15o1, dest=pozycja15)
        final16 = wynikowy_obraz16.resize((360, 425))
        template_image.alpha_composite(final16, dest=pozycja16)
        final18 = wynikowy_obraz18
        template_image.alpha_composite(final18, dest=pozycja18)
        news_button = Image.open("news_button.png").convert("RGBA")
        template_image.alpha_composite(news_button, dest=pozycja17)
        final19 = wynikowy_obraz19
        pozycja19 = (644-math.ceil(int(final19.crop(final19.getbbox()).width) / 2), 1017-math.ceil(int(final19.crop(final19.getbbox()).height)))
        template_image.alpha_composite(final19, dest=pozycja19)
        final20 = wynikowy_obraz20.crop(wynikowy_obraz20.getbbox())
        pozycja20 = (1393-math.ceil(int(final20.width/2)),146-math.ceil(int(final20.height/2)))
        template_image.alpha_composite(final20, dest=pozycja20)
        final21 = wynikowy_obraz21
        template_image.alpha_composite(final21, dest=pozycja21)
        super_overlay = Image.open("super_overlay.png").convert("RGBA")
        template_image.alpha_composite(super_overlay, dest=(879, 178))
        ramka_super = Image.open("super_border.png").convert("RGBA")
        template_image.alpha_composite(ramka_super, dest=(869,174))
        final22 = wynikowy_obraz22.crop(wynikowy_obraz22.getbbox())
        pozycja22 = (1398-math.ceil(int(final22.width/2)),945-math.ceil(int(final22.height/2)))
        template_image.alpha_composite(final22, dest=pozycja22)
        final23 = wynikowy_obraz23.crop(wynikowy_obraz23.getbbox())
        pozycja23 = (1897-math.ceil(int(final23.width)),679)
        template_image.alpha_composite(final23, dest=pozycja23)
        final24 = wynikowy_obraz24.crop(wynikowy_obraz24.getbbox())
        pozycja24 = (1897 - math.ceil(int(final24.width)), 725)
        template_image.alpha_composite(final24, dest=pozycja24)
        template_image.save('generated_image.png')
        result_label.config(text="The final image was generated and saved as generated_image.png")
        img = template_image
        img = img.resize((480, 270))
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img


root = tk.Tk()
root.title("TNO Superevent Creator")
temp = Image.open("template.png")
temp = temp.resize((480, 270))
temp = ImageTk.PhotoImage(temp)
panel = Label(root, image=temp)
panel.grid(column=0, columnspan=2)
tk.Label(root, text="Enter country name:").grid(column=0)
country_entry = tk.Entry(root)
country_entry.grid(column=0)
tk.Button(root, text="Add country name to image", command=add_text_to_img).grid(column=0)
tk.Label(root, text="Enter faction name:").grid(column=0)
faction_entry = tk.Entry(root)
faction_entry.grid(column=0)
tk.Button(root, text="Add faction to image", command=add_text_to_img2).grid(column=0)
selected_option2 = tk.StringVar()  
combobox2 = ttk.Combobox(root, textvariable=selected_option2, values=factions)
combobox2.grid(column=0)
button2 = tk.Button(root, text="Choose faction icon", command=factions_choose)
button2.grid(column=0)
tk.Label(root, text="Enter leader name:").grid(column=0)
leader_entry = tk.Entry(root)
leader_entry.grid(column=0)
tk.Button(root, text="Add leader to image", command=add_text_to_img3).grid(column=0)
tk.Label(root, text="Enter party name:").grid(column=0)
party_entry = tk.Entry(root)
party_entry.grid(column=0)
tk.Button(root, text="Add party to image", command=add_text_to_img4).grid(column=0)
selected_option = tk.StringVar()  
combobox = ttk.Combobox(root, textvariable=selected_option, values=ideologies)
combobox.grid(column=0)
button = tk.Button(root, text="Choose ideology", command=ideologies_choose)
button.grid(column=0)
tk.Label(root, text="Enter ideology name:").grid(column=0)
ideologia_entry = tk.Entry(root)
ideologia_entry.grid(column=0)
tk.Button(root, text="Add ideology name to image", command=add_text_to_img6).grid(column=0)
tk.Label(root, text="Enter next elections date:").grid(column=0)
wybory_entry = tk.Entry(root)
wybory_entry.grid(column=0)
tk.Button(root, text="Add next elections date to image", command=add_text_to_img7).grid(column=0)
tk.Label(root, text="Enter focus name:").grid(column=0)
focus_entry = tk.Entry(root)
focus_entry.grid(column=0)
tk.Button(root, text="Add focus to image", command=add_text_to_img8).grid(column=0)
selected_option_focus = tk.StringVar()  
combobox = ttk.Combobox(root, textvariable=selected_option_focus, values=focuses)
combobox.grid(column=1, row=1)
button = tk.Button(root, text="Choose focus", command=browse_focus)
button.grid(column=1, row=2)
selected_option_flag = tk.StringVar()  
combobox = ttk.Combobox(root, textvariable=selected_option_flag, values=flags)
combobox.grid(column=1, row=3)
button = tk.Button(root, text="Choose flag", command=browse_flag)
button.grid(column=1, row=4)
selected_option_leader = tk.StringVar()  
combobox = ttk.Combobox(root, textvariable=selected_option_leader, values=leaders)
combobox.grid(column=1, row=5)
button = tk.Button(root, text="Choose leader", command=browse_leader)
button.grid(column=1, row=6)
id_en_label = tk.Label(root, text="Enter popularity of 'Esoteric Nazism':")
id_en_label.grid(column=2, row=1)
id_en_entry = tk.Entry(root)
id_en_entry.grid(column=2, row=2)
id_ns_label = tk.Label(root, text="Enter popularity of 'National Socialism':")
id_ns_label.grid(column=2, row=3)
id_ns_entry = tk.Entry(root)
id_ns_entry.grid(column=2, row=4)
id_f_label = tk.Label(root, text="Enter popularity of 'Fascism':")
id_f_label.grid(column=2, row=5)
id_f_entry = tk.Entry(root)
id_f_entry.grid(column=2, row=6)
id_un_label = tk.Label(root, text="Enter popularity of 'Ultranationalism':")
id_un_label.grid(column=2, row=7)
id_un_entry = tk.Entry(root)
id_un_entry.grid(column=2, row=8)
id_d_label = tk.Label(root, text="Enter popularity of 'Despotism':")
id_d_label.grid(column=2, row=9)
id_d_entry = tk.Entry(root)
id_d_entry.grid(column=2, row=10)
id_p_label = tk.Label(root, text="Enter popularity of 'Paternalism':")
id_p_label.grid(column=2, row=11)
id_p_entry = tk.Entry(root)
id_p_entry.grid(column=2, row=12)
id_c_label = tk.Label(root, text="Enter popularity of 'Conservatism':")
id_c_label.grid(column=2, row=13)
id_c_entry = tk.Entry(root)
id_c_entry.grid(column=2, row=14)
id_lc_label = tk.Label(root, text="Enter popularity of 'Liberal Conservatism':")
id_lc_label.grid(column=2, row=15)
id_lc_entry = tk.Entry(root)
id_lc_entry.grid(column=2, row=16)
id_lib_label = tk.Label(root, text="Enter popularity of 'Liberalism':")
id_lib_label.grid(column=2, row=17)
id_lib_entry = tk.Entry(root)
id_lib_entry.grid(column=2, row=18)
id_pr_label = tk.Label(root, text="Enter popularity of 'Progressivism':")
id_pr_label.grid(column=2, row=19)
id_pr_entry = tk.Entry(root)
id_pr_entry.grid(column=2, row=20)
id_s_label = tk.Label(root, text="Enter popularity of 'Socialism':")
id_s_label.grid(column=2, row=21)
id_s_entry = tk.Entry(root)
id_s_entry.grid(column=2, row=22)
id_co_label = tk.Label(root, text="Enter popularity of 'Communism':")
id_co_label.grid(column=2, row=23)
id_co_entry = tk.Entry(root)
id_co_entry.grid(column=2, row=24)
tk.Button(root, text="Add parties' popularities to the image", command=generate_pie_chart).grid(column=2, row=25)
selected_option3 = tk.StringVar()  
combobox3 = ttk.Combobox(root, textvariable=selected_option3, values=headers)
combobox3.grid(column=3, row=1)
button3 = tk.Button(root, text="Choose Newspaper Header", command=header_choose)
button3.grid(column=3, row=2)
tk.Label(root, text="Enter newspaper title:").grid(column=3, row=3)
title_entry = tk.Entry(root)
title_entry.grid(column=3, row=4)
tk.Button(root, text="Add newspaper title to image", command=add_text_to_img15).grid(column=3, row=5)
tk.Label(root, text="Enter newspaper content:").grid(column=3, row=6)
gazeta_entry = ScrolledText(root, width=51, height=20)
gazeta_entry.grid(column=3, row=7, rowspan=15)
tk.Button(root, text="Add newspaper content to image", command=add_text_to_img16).grid(column=3, row=22)
selected_option_news = tk.StringVar()  
combobox = ttk.Combobox(root, textvariable=selected_option_news, values=news_image)
combobox.grid(column=3, row=23)
button = tk.Button(root, text="Choose newspaper image", command=browse_news_img)
button.grid(column=3, row=24)
tk.Label(root, text="Enter newspaper button:").grid(column=3, row=25)
button_news_entry = tk.Entry(root)
button_news_entry.grid(column=3, row=26)
tk.Button(root, text="Add newspaper button to image", command=add_text_to_img19).grid(column=3, row=27)
tk.Label(root, text="Enter superevent title").grid(column=4, row=1)
title_sup_entry = tk.Entry(root)
title_sup_entry.grid(column=4, row=2)
tk.Button(root, text="Add the superevent title to image", command=add_text_to_img20).grid(column=4, row=3)
selected_option_super = tk.StringVar()  
combobox = ttk.Combobox(root, textvariable=selected_option_super, values=superevent_image)
combobox.grid(column=4, row=4)
button = tk.Button(root, text="Choose superevent image", command=browse_super_img)
button.grid(column=4, row=5)
tk.Label(root, text="Enter superevent quote").grid(column=4, row=9)
quote_sup_entry = tk.Entry(root)
quote_sup_entry.grid(column=4, row=10)
tk.Button(root, text="Add the superevent quote to image", command=add_text_to_img22).grid(column=4, row=11)
tk.Label(root, text="Enter superevent quote author").grid(column=4, row=12)
author_sup_entry = tk.Entry(root)
author_sup_entry.grid(column=4, row=13)
tk.Button(root, text="Add the superevent quote author to image", command=add_text_to_img23).grid(column=4, row=14)
tk.Label(root, text="Enter superevent button").grid(column=4, row=6)
button_sup_entry = tk.Entry(root)
button_sup_entry.grid(column=4, row=7)
tk.Button(root, text="Add the superevent button to image", command=add_text_to_img21).grid(column=4, row=8)
tk.Button(root, text="Generate the image", command=generate_final_image).grid(column=0)
result_label = tk.Label(root, text="")
result_label.grid(column=0)
root.mainloop()