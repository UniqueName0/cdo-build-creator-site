from flask import Flask, request, redirect
from markupsafe import escape
import os
import numpy as np

try:
    from PIL import Image
except ImportError:
    import Image

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"<p>create a build at <a href ='/create-build'>/create-build</a></p><p>github for this site: <a href='https://github.com/UniqueName0/cdo-build-creator-site'>https://github.com/UniqueName0/cdo-build-creator-site</a></p>"


@app.route("/<character>+<runebuild>+<enhancements>+<relic1>+<relic2>+<relic3>")
def build(character, runebuild, relic1, relic2, relic3, enhancements):


    # runes
    runePositions = [(53, 62), (232, 62), (14, 144), (96, 144), (190, 144), (270, 144), (52, 223), (232, 223), (134, 23), (134, 245)]
    runesImg = Image.open("images/empty-runes.png")
    for x in range(len(runebuild)):
        if runebuild[x] == "A":
            rune = Image.open("images/dmg-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "S":
            rune = Image.open("images/aspd-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "M":
            rune = Image.open("images/mspd-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "H":
            rune = Image.open("images/hp-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "C":
            rune = Image.open("images/cd-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "L":
            rune = Image.open("images/ls-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "D":
            rune = Image.open("images/def-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "R":
            rune = Image.open("images/rec-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "X":
            rune = Image.open("images/xp-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "Q":
            rune = Image.open("images/crit-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
        elif runebuild[x] == "P":
            rune = Image.open("images/res-rune.png")
            if x > 7:
                rune = rune.resize((80, 80))
            runesImg.paste(rune, runePositions[x], rune)
    runesImg.save("static/runes.png")

    # enhancements
    enhanceAPositions = [(145, -1), (295, -1), (444, -1), (593,-1), (742, -1)]
    enhanceBPositions = [(145, 102), (295, 102), (444, 102), (593, 102), (742, 102)]
    enhanceImg = Image.open(f'images/empty{character}enhancements.png')
    checkImg = Image.open("images/check.png")
    for x in range(len(enhancements)):
        if enhancements[x] == "A":
            enhanceImg.paste(checkImg, enhanceAPositions[x], checkImg)
        elif enhancements[x] == "B":
            enhanceImg.paste(checkImg, enhanceBPositions[x], checkImg)
    enhanceImg.save("static/enhancements.png")

    return f'<h1>{character} build</h1><h1>Runes</h1><img src="/static/runes.png"><h1>Relics</h1><img style="float:left;width:30%;" src="/static/{relic1}.png"><img style="float:left;width:30%;" src="/static/{relic2}.png"><img style="float:left;width:30%;" src="/static/{relic3}.png"><h1>enhancements</h1><img src="/static/enhancements.png"><br><h1>to share this build just copy the link</h1>'


@app.route('/create-build')
def form():
    return '''<form action="/data" method = "POST">
    <label for="char">character</label>
  <select id="char" name="char">
    <option value="berserker">Berserker</option>
    <option value="magician">Magician</option>
    <option value="knight">Knight</option>
    <option value="priest">Priest</option>
    <option value="engineer">Engineer</option>
    <option value="samurai">Samurai</option>
    <option value="lancer">Lancer</option>
    <option value="guardian">Guardian</option>
    <option value="fighter">Fighter</option>
    <option value="necromancer">Necromancer</option>
    <option value="druid">Druid</option>
    <option value=wizard">Wizard</option>
    <option value="chef">Chef</option>
    <option value="archer">Archer</option>
    <option value="musketeer">Musketeer</option>
    <option value="rogue">Rogue</option>
    <option value="pierrot">Pierrot</option>
    <option value="bard">Bard</option>
  </select>
  <br>
    <label for="r9">level 5 rune</label>
  <select id="r9" name="r9">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="r10">level 5 rune</label>
  <select id="r10" name="r10">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="r1">level 4 rune</label>
  <select id="r1" name="r1">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="r2">level 4 rune</label>
  <select id="r2" name="r2">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="r3">level 4 rune</label>
  <select id="r3" name="r3">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="r4">level 4 rune</label>
  <select id="r4" name="r4">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="r5">level 4 rune</label>
  <select id="r5" name="r5">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="r6">level 4 rune</label>
  <select id="r6" name="r6">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="r7">level 4 rune</label>
  <select id="r7" name="r7">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="r8">level 4 rune</label>
  <select id="r8" name="r8">
    <option value="A">attack damage</option>
    <option value="S">attack speed</option>
    <option value="M">move speed</option>
    <option value="H">health</option>
    <option value="C">cool down reduction</option>
    <option value="L">lifesteal</option>
    <option value="D">defense</option>
    <option value="R">recovery</option>
    <option value="X">xp gain</option>
    <option value="Q">crit chance</option>
    <option value="P">respawn time</option>
  </select>
  <br>
  <label for="e1">enhancement 1</label>
  <select id="e1" name="e1">
    <option value="A">A</option>
    <option value="B">B</option>
  </select>
  <br>
  <label for="e2">enhancement 2</label>
  <select id="e2" name="e2">
    <option value="A">A</option>
    <option value="B">B</option>
  </select>
  <br>
  <label for="e3">enhancement 3</label>
  <select id="e3" name="e3">
    <option value="A">A</option>
    <option value="B">B</option>
  </select>
  <br>
  <label for="e4">enhancement 4</label>
  <select id="e4" name="e4">
    <option value="A">A</option>
    <option value="B">B</option>
  </select>
  <br>
  <label for="e5">enhancement 5</label>
  <select id="e5" name="e5">
    <option value="A">A</option>
    <option value="B">B</option>
  </select>
  <br>
  <label for="relic1">relic</label>
  <select id="relic1" name="relic1">
    <option value="aegis">Aegis</option>
    <option value="achilles">Achilles</option>
    <option value="durandal">Durandal</option> 
    <option value="fail_note">Fail Note</option>
    <option value="moln">Moln</option>
    <option value="hildegrim">Hildegrim</option>
    <option value="dragon_crescent_blade">Dragon Crescent Blade</option>
    <option value="ruyi_bang">Ruyi Bang</option>
    <option value="caladborg">Caladborg</option> 
    <option value="daitsuren">daitsuren</option>
    <option value="galatin">Galatin</option>
    <option value="plum_blossom">Plum Blossom</option>
    <option value="mistelten">Mistelten</option>
    <option value="levatein">Levatein</option>
    <option value="barissida">Barissida</option>
    <option value="aaronite">Aaronite</option>
    <option value="kusanagis_blade">Kusanagi's Blade</option>
    <option value="heaven_reliant_sword">Heaven Reliant Sword</option>
    <option value="nether_strand">Nether Strand</option>
    <option value="sorcerers_stone">Sorcerer's Stone</option>
    <option value="magic_lamp">Magic Lamp</option>
    <option value="pandoras_box">Pandora's Box</option>
    <option value="caduceus">Caduceus</option>
    <option value="princess_iron_fan">Princess Iron Fan</option>
    <option value="akashic_records">Akashic Records</option>
    <option value="ascalan">Ascalan</option>
    <option value="book_of_thoth">Book Of Thoth</option>
    <option value="exalibur">Excalibur</option>
    <option value="seal_of_solomon">Seal Of Solomon</option>
    <option value="imperial_jade_seal">Imperial Jade Seal</option>
    <option value="gungnir">Gungnir</option>
    <option value="brans_cauldron">Bran's Cauldron</option>
    <option value="ankh">Ankh</option>
    <option value="trident">Trident</option>
    <option value="golden_apple">Golden Apple</option>
    <option value="ambrosia">Ambrosia</option>
    <option value="anquila">Anquila</option>
    <option value="nemean_lionskin">Nemean Lionskin</option>
    <option value="aias_shield">Aias Shield</option>
    <option value="angelic_jade_belt">Angelic Jade Belt</option>
  </select>
  <br>
  <label for="relic2">relic</label>
  <select id="relic2" name="relic2">
    <option value="aegis">Aegis</option>
    <option value="achilles">Achilles</option>
    <option value="durandal">Durandal</option> 
    <option value="fail_note">Fail Note</option>
    <option value="moln">Moln</option>
    <option value="hildegrim">Hildegrim</option>
    <option value="dragon_crescent_blade">Dragon Crescent Blade</option>
    <option value="ruyi_bang">Ruyi Bang</option>
    <option value="caladborg">Caladborg</option> 
    <option value="daitsuren">daitsuren</option>
    <option value="galatin">Galatin</option>
    <option value="plum_blossom">Plum Blossom</option>
    <option value="mistelten">Mistelten</option>
    <option value="levatein">Levatein</option>
    <option value="barissida">Barissida</option>
    <option value="aaronite">Aaronite</option>
    <option value="kusanagis_blade">Kusanagi's Blade</option>
    <option value="heaven_reliant_sword">Heaven Reliant Sword</option>
    <option value="nether_strand">Nether Strand</option>
    <option value="sorcerers_stone">Sorcerer's Stone</option>
    <option value="magic_lamp">Magic Lamp</option>
    <option value="pandoras_box">Pandora's Box</option>
    <option value="caduceus">Caduceus</option>
    <option value="princess_iron_fan">Princess Iron Fan</option>
    <option value="akashic_records">Akashic Records</option>
    <option value="ascalan">Ascalan</option>
    <option value="book_of_thoth">Book Of Thoth</option>
    <option value="exalibur">Excalibur</option>
    <option value="seal_of_solomon">Seal Of Solomon</option>
    <option value="imperial_jade_seal">Imperial Jade Seal</option>
    <option value="gungnir">Gungnir</option>
    <option value="brans_cauldron">Bran's Cauldron</option>
    <option value="ankh">Ankh</option>
    <option value="trident">Trident</option>
    <option value="golden_apple">Golden Apple</option>
    <option value="ambrosia">Ambrosia</option>
    <option value="anquila">Anquila</option>
    <option value="nemean_lionskin">Nemean Lionskin</option>
    <option value="aias_shield">Aias Shield</option>
    <option value="angelic_jade_belt">Angelic Jade Belt</option>
  </select>
  <br>
  <label for="relic3">relic</label>
  <select id="relic3" name="relic3">
    <option value="aegis">Aegis</option>
    <option value="achilles">Achilles</option>
    <option value="durandal">Durandal</option> 
    <option value="fail_note">Fail Note</option>
    <option value="moln">Moln</option>
    <option value="hildegrim">Hildegrim</option>
    <option value="dragon_crescent_blade">Dragon Crescent Blade</option>
    <option value="ruyi_bang">Ruyi Bang</option>
    <option value="caladborg">Caladborg</option> 
    <option value="daitsuren">daitsuren</option>
    <option value="galatin">Galatin</option>
    <option value="plum_blossom">Plum Blossom</option>
    <option value="mistelten">Mistelten</option>
    <option value="levatein">Levatein</option>
    <option value="barissida">Barissida</option>
    <option value="aaronite">Aaronite</option>
    <option value="kusanagis_blade">Kusanagi's Blade</option>
    <option value="heaven_reliant_sword">Heaven Reliant Sword</option>
    <option value="nether_strand">Nether Strand</option>
    <option value="sorcerers_stone">Sorcerer's Stone</option>
    <option value="magic_lamp">Magic Lamp</option>
    <option value="pandoras_box">Pandora's Box</option>
    <option value="caduceus">Caduceus</option>
    <option value="princess_iron_fan">Princess Iron Fan</option>
    <option value="akashic_records">Akashic Records</option>
    <option value="ascalan">Ascalan</option>
    <option value="book_of_thoth">Book Of Thoth</option>
    <option value="exalibur">Excalibur</option>
    <option value="seal_of_solomon">Seal Of Solomon</option>
    <option value="imperial_jade_seal">Imperial Jade Seal</option>
    <option value="gungnir">Gungnir</option>
    <option value="brans_cauldron">Bran's Cauldron</option>
    <option value="ankh">Ankh</option>
    <option value="trident">Trident</option>
    <option value="golden_apple">Golden Apple</option>
    <option value="ambrosia">Ambrosia</option>
    <option value="anquila">Anquila</option>
    <option value="nemean_lionskin">Nemean Lionskin</option>
    <option value="aias_shield">Aias Shield</option>
    <option value="angelic_jade_belt">Angelic Jade Belt</option>
  </select>
    <p><input type = "submit" value = "Submit" /></p>
</form>'''


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/create-build' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return redirect(f'/{form_data["char"]}+{form_data["r1"]}{form_data["r2"]}{form_data["r3"]}{form_data["r4"]}{form_data["r5"]}{form_data["r6"]}{form_data["r7"]}{form_data["r8"]}{form_data["r9"]}{form_data["r10"]}+{form_data["e1"]}{form_data["e2"]}{form_data["e3"]}{form_data["e4"]}{form_data["e5"]}+{form_data["relic1"]}+{form_data["relic2"]}+{form_data["relic3"]}'
, code=302)
