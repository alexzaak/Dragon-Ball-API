# coding: UTF-8
from django.shortcuts import render
from character.models import character
from character.models import type_character
from sagas.models import saga
from fusion.models import type_fusion
from fusion.models import fusion
from django.http import HttpResponse
import json

# Create your views here.
def get_all_types(request):
    alltypes = type_character.objects.all()
    races = []
    for tipo in alltypes:
        race = {}
        race["id"] = tipo.id
        race["race"] = tipo.nm_type_character
        races.append(race)
        
    return HttpResponse(json.dumps(races), content_type='application/json')

def get_type(request, type_character_id):
    tipo = type_character.objects.get(id=int(type_character_id))
    race = {}
    race["id"]=tipo.id
    race["nm_type_character"]= tipo.nm_type_character
    
    return HttpResponse(json.dumps(race), content_type='application/json')

def get_character_by_saga_id(request, id_saga): 
    characters = character.objects.filter(saga_id=int(id_saga))
    personagens = []
    for chares in characters:
        charc = {}
        charc["id"] = chares.id
        charc["nm_character"] = chares.nm_character
        charc["img_character"]= chares.img_character
        charc["fighting_power"]= chares.fighting_power
        charc["saga"]= saga.objects.get(id=int(chares.saga_id_id)).nm_saga
        charc["saga_id"]= int(chares.saga_id_id)
        charc["race"]= type_character.objects.get(id=int(chares.type_id_id)).nm_type_character
        personagens.append(charc)
    return HttpResponse(json.dumps(personagens), content_type='application/json')

def get_characters(request):
    allcharacters = character.objects.all()
    personagens = []
    for chares in allcharacters:
        charc = {}
        charc["id"] = chares.id
        charc["nm_character"] = chares.nm_character
        charc["img_character"]= chares.img_character
        charc["fighting_power"]= chares.fighting_power
        charc["saga"]= saga.objects.get(id=int(chares.saga_id_id)).nm_saga
        charc["saga_id"]= int(chares.saga_id_id)
        charc["race"]= type_character.objects.get(id=int(chares.type_id_id)).nm_type_character
        personagens.append(charc)
    return HttpResponse(json.dumps(personagens), content_type='application/json')

def get_character(request,name_or_id):
    result = {}
    if name_or_id.isnumeric():
        allcharacters = character.objects.get(id=int(name_or_id))
        result["id"] = allcharacters.id
        result["nm_character"] = allcharacters.nm_character
        result["img_character"] = allcharacters.img_character
        result["fighting_power"] = allcharacters.fighting_power
        result["race"] = type_character.objects.get(id=int(allcharacters.type_id_id)).nm_type_character
        result["saga"] = saga.objects.get(id=int(allcharacters.saga_id_id)).nm_saga
    else:
        alllike = []
        allcharacters = character.objects.filter(string__contains=name_or_id)
        for chares in allcharacters:
            charc = {}
            charc["id"] = chares.id
            charc["nm_character"] = chares.nm_character
            charc["img_character"]= chares.img_character
            charc["fighting_power"]= chares.fighting_power
            charc["race"]= type_character.objects.get(id=int(chares.type_id_id)).nm_type_character
            charc["saga"]= saga.objects.get(id=int(chares.saga_id_id)).nm_saga
            charc["saga_id"]= int(chares.saga_id_id)
            alllike.append(chares)
        result["characters"] = alllike
    return HttpResponse(json.dumps(result), content_type='application/json')
    
def seeds(request):
    
    sg1 = saga(
        nm_saga="Dragon Ball",
        ds_saga="Dragon Ball ist die erste von drei Fernsehserien, die auf dem gleichnamigen Manga von Akira Toriyama basieren. Für die Erstausstrahlung im japanischen Fernsehen auf dem Fernsehsender Fuji TV vom 26. Februar 1986 bis 12. April 1989 wurden vom Animationsstudio Toei insgesamt 153 Episoden produziert, die weltweit exportiert und durch eine angepasste Synchronisation in lokalen Fernsehstationen ausgestrahlt wurden. Zusätzlich zu der Fernsehserie wurden noch vier Kinofilme produziert. Die Handlung wird in der Fernsehserie Dragon Ball Z fortgesetzt, die ebenfalls auf dem Manga basiert.",
        img_saga="https://i.pinimg.com/originals/77/82/f0/7782f08f34d373c4caf42aee9160a32d.jpg")
    sg1.save()

    sg2 = saga(
        nm_saga="Dragon Ball Z",
        ds_saga="Dragon Ball Z ist eine japanische 291 Episoden umfassende Animeserie, die dem Shōnen-Genre zuzuordnen ist und die Fortsetzung der Fernsehserie Dragon Ball darstellt. Beide Animes beruhen auf der von 1984 bis 1995 erschienenen, international erfolgreichen 42-bändigen Manga-Serie Dragon Ball des Zeichners Akira Toriyama. Während der Dragon-Ball-Anime die Manga-Handlung bis Band 17, Kapitel 194 umsetzt und Geschehnisse in der Kindheit der Hauptfigur Son-Goku schildert, führt Dragon Ball Z die Geschichte mit Son-Goku als Erwachsenem ab Band 17, Kapitel 195 weiter.",
        img_saga="http://ptanime.com/wp-content/uploads/2015/05/Dragon_Ball_Z_Analise_Imagem_Saga_Majin_Buu.jpg")
    sg2.save()
    sg3 = saga(
        nm_saga="Dragon Ball GT",
        ds_saga="Dragon Ball GT ist die zweite Fortsetzungsserie der Animeserie Dragon Ball. Sie wurde von Beginn an als Anime konzipiert und basiert nicht, wie die vorhergehenden Animeserien Dragon Ball und Dragon Ball Z, auf der Originalhandlung des Mangas des japanischen Zeichners Akira Toriyama. Toriyama wirkte bei Dragon Ball GT lediglich als künstlerischer Berater mit.",
        img_saga="https://vignette2.wikia.nocookie.net/dbz-dokkanbattle/images/9/95/Black_Star_DB_Saga.png/revision/latest?cb=20160910202651")
    sg3.save()
    sg4 = saga(
        nm_saga="Dragon Ball Super",
        ds_saga="Dragon Ball Super ist eine Animeserie, die von Tōei Animation produziert wird. Die erste Folge wurde am 5. Juli 2015 ausgestrahlt. Sie ist der direkte Nachfolger zu Dragon Ball Z. Die Handlung spielt in der zehn Jahre umfassenden Lücke zwischen dem Sieg über Boo und dem Turnier, bei dem Son Goku auf Boos Wiedergeburt Oob trifft. Die Handlung beginnt 4 Jahre nach dem Sieg über Boo. Bei den ersten 27 Folgen handelt es sich inhaltlich um Neuerzählungen der Filme Kampf der Götter und Resurrection ‚F‘.",
        img_saga="https://i.pinimg.com/originals/81/57/19/81571933f0d137e2d6c98304e0376311.png")
    sg4.save()

    sg5 = saga(
        nm_saga="Dragon Ball AF",
        ds_saga="Dragonball AF ist eine Art Fan-Fiction über den Manga und Anime Dragonball von Akira Toriyama, der darauf folgte, dass viele Fans sehr traurig darüber waren, dass Dragonball mit Dragonball GT als beendet galt. AF steht dabei für After Future. Manche Leute glauben, dass Dragonball AF auch wirklich existiert, aber das ist wohl jedem selbst überlassen. Im Internet geistert dieser Begriff allerdings schon seit mehreren Jahren umher und gewann so mehr und mehr an Bekanntheit, sodass immer mehr Seiten auf Dragonball AF hinweisen und sehr viele Bilder und Ähnliches entstanden.",
        img_saga="https://i.ytimg.com/vi/-xNbJ803Kkw/maxresdefault.jpg")
    sg5.save()

    tpf = type_fusion(nm_type_fusion="Potara Fusion")
    tpf.save()
    tpf2 = type_fusion(nm_type_fusion="Fusionstanz")
    tpf2.save()

    tpp = type_character(nm_type_character="Mensch")
    tpp.save()
    tpp = type_character(nm_type_character="Saiyajin")
    tpp.save()
    tpp = type_character(nm_type_character="Namikianer")
    tpp.save()
    tpp = type_character(nm_type_character="Android")
    tpp.save()
    tpp = type_character(nm_type_character="Majin")
    tpp.save()

    p = character(
        nm_character="Kid Goku",
        img_character="http://www.imagenswiki.com/Uploads/imagenswiki.com/ImagensGrandes/son-goku-crianca.jpg",
        fighting_power="260")
    p.type_id_id = 2
    p.saga_id = sg1
    p.save()
    p = character(
        nm_character="Goku",
        img_character="https://vignette.wikia.nocookie.net/dragonball/images/5/5b/Gokusteppingoutofaspaceship.jpg/revision/latest/scale-to-width-down/224?cb=20150325220848",
        fighting_power="924")
    p.type_id_id = 2
    p.saga_id = sg2
    p.save()
    p = character(
        nm_character="Goku Super Saiyajin 1",
        img_character="https://dreager1.files.wordpress.com/2011/08/snap2149516qs7.jpg",
        fighting_power="150000000")
    p.type_id_id = 2
    p.saga_id = sg2
    p.save()
    p = character(
        nm_character="Goku Super Saiyajin 2",
        img_character="https://vignette.wikia.nocookie.net/dragonball/images/a/ac/Goku-Super-Saiyan-2-.jpg/revision/latest?cb=20110426171840",
        fighting_power="6000000000")
    p.type_id_id = 2
    p.saga_id = sg2
    p.save()
    p = character(
        nm_character="Goku Super Saiyajin 3",
        img_character="https://vignette2.wikia.nocookie.net/dragonuniverse/images/8/89/SSJ3.png/revision/latest?cb=20160928233848",
        fighting_power="10000000000")
    p.type_id_id = 2
    p.saga_id = sg2
    p.save()
    goku = character(
        nm_character="Goku",
        img_character="https://vignette.wikia.nocookie.net/dragonball/images/5/5b/Gokusteppingoutofaspaceship.jpg/revision/latest/scale-to-width-down/224?cb=20150325220848",
        fighting_power="924")
    goku.type_id_id = 2
    goku.saga_id_id = 4
    goku.save()
    p = character(
        nm_character="Goku Super Saiyajin 1",
        img_character="https://dreager1.files.wordpress.com/2011/08/snap2149516qs7.jpg",
        fighting_power="150000000")
    p.type_id_id = 2
    p.saga_id_id = 4
    p.save()
    p = character(
        nm_character="Goku Super Saiyajin 2",
        img_character="https://vignette.wikia.nocookie.net/dragonball/images/a/ac/Goku-Super-Saiyan-2-.jpg/revision/latest?cb=20110426171840",fighting_power="6000000000")
    p.type_id_id = 2
    p.saga_id_id = 4
    p.save()
    p = character(nm_character="Goku Super Saiyajin 3",img_character="https://vignette2.wikia.nocookie.net/dragonuniverse/images/8/89/SSJ3.png/revision/latest?cb=20160928233848",fighting_power="10000000000")
    p.type_id_id = 2
    p.saga_id_id = 4
    p.save()
    p = character(nm_character="Goku Super Saiyajin Blue",img_character="http://vignette1.wikia.nocookie.net/dragonball/images/1/12/SSGSS_GOKU.png/revision/latest?cb=20151025084338",fighting_power="100000000000")
    p.type_id_id = 2
    p.saga_id_id = 4
    p.save()
    p = character(nm_character="(GT) Goku",img_character="https://i.stack.imgur.com/6HrTE.jpg",fighting_power="10000000")
    p.type_id_id = 2
    p.saga_id_id = 3
    p.save()
    p = character(nm_character="(GT) Goku Super Saiyajin 1",img_character="https://static.comicvine.com/uploads/original/14/149746/3647183-4101411823-Goku_.jpg",fighting_power="150000000")
    p.type_id_id = 2
    p.saga_id_id = 3
    p.save()
    p = character(nm_character="(GT) Goku Super Saiyajin 2",img_character="http://vignette2.wikia.nocookie.net/dragonball/images/7/7f/GT_Kid_Goku_Super_Saiyan_2_by_dbzataricommunity.jpg/revision/latest?cb=20110412181525",fighting_power="6000000000")
    p.type_id_id = 2
    p.saga_id_id = 3
    p.save()
    p = character(nm_character="(GT) Goku Super Saiyajin 3",img_character="http://pm1.narvii.com/6152/0abf4a01f38c1f84e7ea32e9601aaa1575b93e7e_hq.jpg",fighting_power="10000000000")
    p.type_id_id = 2
    p.saga_id_id = 3
    p.save()
    p = character(nm_character="Goku Super Saiyajin 4",img_character="http://vignette4.wikia.nocookie.net/p__/images/f/f1/Goku_Super_Saiyan_4.png/revision/latest?cb=20130805024507&path-prefix=protagonist",fighting_power="100000000000")
    p.type_id_id = 2
    p.saga_id_id = 3
    p.save()
    p = character(nm_character="Vegeta",img_character="https://upload.wikimedia.org/wikipedia/en/8/88/Vegeta_Dragon_Ball.jpg",fighting_power="1200")
    p.type_id_id = 2
    p.saga_id_id = 2
    p.save()
    p = character(nm_character="Vegeta Super Saiyajin 1",img_character="https://vignette.wikia.nocookie.net/dragonball/images/6/6b/Vegeta_becomes_Super_Saiyan.JPG/revision/latest?cb=20120214203120",fighting_power="2200")
    p.type_id_id = 2
    p.saga_id_id = 2
    p.save()
    p = character(nm_character="Vegeta Super Saiyajin 2",img_character="https://i.pinimg.com/originals/94/f3/b7/94f3b7f8bbda987da4eaa53e2cc99655.jpg",fighting_power="")
    p.type_id_id = 2
    p.saga_id_id = 2
    p.save()
    p = character(nm_character="Vegeta",img_character="",fighting_power="")
    p.type_id_id = 2
    p.saga_id_id = 3
    p.save()
    p = character(nm_character="Vegeta Super Saiyajin 1",img_character="",fighting_power="")
    p.type_id_id = 2
    p.saga_id_id = 3
    p.save()
    p = character(nm_character="Vegeta Super Saiyajin 2",img_character="",fighting_power="")
    p.type_id_id = 2
    p.saga_id_id = 3
    p.save()
    p = character(nm_character="Vegeta Super Saiyajin 4",img_character="https://vignette2.wikia.nocookie.net/poohadventures/images/4/40/Vegeta-super-saiyan-4.jpg/revision/latest?cb=20150403211313",fighting_power="")
    p.type_id_id = 2
    p.saga_id_id = 2
    p.save()
    vegeta = character(nm_character="Vegeta",img_character="",fighting_power="")
    vegeta.type_id_id = 2
    vegeta.saga_id_id = 4
    vegeta.save()
    p = character(nm_character="Vegeta Super Saiyajin 1",img_character="",fighting_power="")
    p.type_id_id = 2
    p.saga_id_id = 4
    p.save()
    p = character(nm_character="Vegeta Super Saiyajin 2",img_character="",fighting_power="")
    p.type_id_id = 2
    p.saga_id_id = 4
    p.save()
    p = character(nm_character="Vegeta Super Saiyajin Blue",img_character="https://res.cloudinary.com/jerrick/image/upload/f_auto,fl_progressive,q_auto,c_fit,w_1140/a54xtelfenxa1wyidccv",fighting_power="")
    p.type_id_id = 2
    p.saga_id_id = 4
    p.save()
    
    tp = fusion(type_fusion_id=tpf,character1_id=goku,character2_id=vegeta,nm_character_fusion="Vegetto")
    tp.character1_id_id = 2
    tp.character2_id_id = 15
    tp.type_fusion_id_id = 1
    tp.save()
    tp = fusion(type_fusion_id=tpf2,character1_id=goku,character2_id=vegeta,nm_character_fusion="Gojeta")
    tp.character1_id_id = 14
    tp.character2_id_id = 21
    tp.type_fusion_id_id = 2
    tp.save()
    
    return HttpResponse("201")