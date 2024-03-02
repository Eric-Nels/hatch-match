#!/usr/bin/env python3

from DB.flies import Flies
from DB.suggestions import Suggestions
from DB.bugs import Bugs

def seed_database():
    try:
        Flies.drop_table()
        Flies.create_table()

        Suggestions.drop_table()
        Suggestions.create_table()

        Bugs.drop_table()
        Bugs.create_table()

        Bugs.create("Mayfly", "Nymph", "https://www.teatown.org/wp-content/uploads/2020/05/5789175336_758e4c82e7_b.jpg")
        Bugs.create("Mayfly", "Emerger", "https://blog.fullingmill.com/wp-content/uploads/2022/05/Photo-2.jpg")
        Bugs.create("Mayfly", "Adult", "https://www.nwf.org/-/media/NEW-WEBSITE/Shared-Folder/Wildlife/Invertebrates/invertebrate_mayflies_600x300.jpg")
        Bugs.create("Caddis", "Nymph", "https://ascentflyfishing.com/product_images/uploaded_images/caddis-larva-cased-caddis.jpg")
        Bugs.create("Caddis", "Emerger", "https://www.riseformflyfishing.com/Site/images/hatches/caddis_giant_casemaker_pupa.jpg")
        Bugs.create("Caddis", "Adult", "https://cdn.britannica.com/15/137315-050-70C02BDD/Adult-caddisfly.jpg")
        Bugs.create("Stonefly", "Nymph", "https://news.orvis.com/wp-content/uploads/2018/05/stonefly1.jpg")
        Bugs.create("Stonefly", "Adult", "https://ars.els-cdn.com/content/image/3-s2.0-B978012370626300185X-gr5.jpg")
        Bugs.create("Midge", "Adult", "https://www.flyfishersatthecrossing.org/wp-content/uploads/2018/03/MIdge.jpg")
        

        Flies.create("RiverKeeper Soft Hackle Cripple", "https://www.johnkreft.com/wp-content/uploads/2020/01/RiverKeeper-Soft-Hackle-Cripple-PMD.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("Sparkle Dun PMD", "https://www.johnkreft.com/wp-content/uploads/2016/11/Sparkle-Dun-PMD.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Improved Sparkle Dun BWO", "https://www.johnkreft.com/wp-content/uploads/2016/11/Improved-Sparkle-Dun-BWO.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Green Drake Sparkle Dun", "https://www.johnkreft.com/wp-content/uploads/2019/10/Sparkle-Dun-Green-Drake.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("BWO – CDC & biot", "https://www.johnkreft.com/wp-content/uploads/2017/03/BWO-CDC-Biot.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("BWO Mayfly Cripple", "https://www.johnkreft.com/wp-content/uploads/BWO-Mayfly-Cripple.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("BWO Parachute", "https://www.johnkreft.com/wp-content/uploads/2017/09/Blue-Wing-Olive-1.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Caudatella Mayfly Cripple", "https://www.johnkreft.com/wp-content/uploads/2014/05/Caudatella-Mayfly-Cripple-1024x838.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("March Brown Comparadun", "https://www.johnkreft.com/wp-content/uploads/Comparadun-Mahogany.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("PMD Parachute", "https://www.johnkreft.com/wp-content/uploads/2017/10/Parachute-PMD-Dry-Fly.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Mayfly Cripple", "https://www.johnkreft.com/wp-content/uploads/2014/05/PMD-Mayfly-Cripple1-1024x808.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Parachute Adams", "https://www.johnkreft.com/wp-content/uploads/2019/02/Parachute-Adams-1.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Rusty Paraspinner", "https://www.johnkreft.com/wp-content/uploads/2014/03/Rusty-Paraspinner-1024x661.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Rusty Spinner – Biot Body", "https://www.johnkreft.com/wp-content/uploads/2020/05/Rusty-Spinner-Biot-Body.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("RS2", "https://www.johnkreft.com/wp-content/uploads/2018/11/RS2-Grey.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Purple Haze", "https://www.johnkreft.com/wp-content/uploads/2018/01/Purple-Haze-1.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("PMD Foam Emerger PMD", "https://www.johnkreft.com/wp-content/uploads/2015/09/PMD-Foam-Emerger.jpg.webp", "Dry", "Mayfly", "Emerger")
        Flies.create("Improved Sparkle Dun PMD", "https://www.johnkreft.com/wp-content/uploads/2017/04/Improved-Sparkle-Dun-PMD.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Green Drake Hairwing Dun", "https://www.johnkreft.com/wp-content/uploads/2016/02/Green-Drake-Hairwing-Dun.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Lempke Extended Body Green Drake", "https://www.johnkreft.com/wp-content/uploads/2017/01/Lempke-Extended-Body-Green-Drake.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Green Drake CDC Loop Wing Emerger", "https://www.johnkreft.com/wp-content/uploads/2017/02/Stalcup-CDC-Loop-Wing-Emerger.jpg.webp", "Dry", "Mayfly", "Emerger")
        Flies.create("Last Chance Cripple Baetis", "https://www.johnkreft.com/wp-content/uploads/2017/02/Last-Chance-Cripple-Baetis.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("March Brown Cripple", "https://www.johnkreft.com/wp-content/uploads/2017/02/Mayfly-Cripple-Cinygmula.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Hatchmaster Green Drake", "https://www.johnkreft.com/wp-content/uploads/2017/04/Hatchmaster-Green-Drake.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Dark Haystack", "https://www.johnkreft.com/wp-content/uploads/2017/09/Haystack.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Green Drake Klinkhåmer Variant", "https://www.johnkreft.com/wp-content/uploads/2017/09/Green-Drake-Klinkh%C3%A5mer-Variant.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("BWO Klinkhamer Variant", "https://www.johnkreft.com/wp-content/uploads/2017/10/BWO-Klinkhamer-Variant.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Medallion Biot Green Drake Wet Fly", "https://www.johnkreft.com/wp-content/uploads/2017/03/Medallion-Biot-Wet-Fly.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Quigley Hackle Stacker", "https://www.johnkreft.com/wp-content/uploads/2016/05/Quigleys-PMD-Hackle-Stacker.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Green Drake CDC Loop Wing Emerger", "https://www.johnkreft.com/wp-content/uploads/Green-Drake-CDC-Loop-Wing-Emerger.jpg.webp", "Dry", "Mayfly", "Emerger")
        Flies.create("Stalcup’s CDC Loop Wing Emerger", "https://www.johnkreft.com/wp-content/uploads/2018/03/Stalcups-CDC-Loop-Wing-Emerger.jpg.webp", "Dry", "Mayfly", "Emerger")
        Flies.create("Galloup’s Found Link", "https://www.johnkreft.com/wp-content/uploads/2018/04/Galloups-Found-Link.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Epeorus Spinner", "https://www.johnkreft.com/wp-content/uploads/2018/08/Epeorus-Spinner.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Quigley Cripple", "https://www.johnkreft.com/wp-content/uploads/2019/01/Quigley-Cripple-PMD-Version.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Quigley Gray Drake Cripple", "https://www.johnkreft.com/wp-content/uploads/Quigley-Cripple-Gray-Drake.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Quigley Cripple Red Quill", "https://www.johnkreft.com/wp-content/uploads/Quigley-Cripple-Red-Quill.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("Film Critic Green Drake", "https://www.johnkreft.com/wp-content/uploads/2019/05/Film-Critic-Green-Drake.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Quigley March Brown Hackle Stacker", "https://www.johnkreft.com/wp-content/uploads/2019/02/March-Brown-Hackle-Stacker.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Quigley Film Critic BWO", "https://www.johnkreft.com/wp-content/uploads/2019/04/Film-Critic-BWO.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Quigley Film Critic – PMD", "https://www.johnkreft.com/wp-content/uploads/2019/04/Film-Critic-PMD.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Galloup’s Compara Spinner – PMD", "https://www.johnkreft.com/wp-content/uploads/Galloups-Compara-Spinner-Biot-Body-1024x683.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Black Wing Baetis Cripple", "https://www.johnkreft.com/wp-content/uploads/2017/08/Galloups-Compara-Spinner.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("IOBO Humpy", "https://www.johnkreft.com/wp-content/uploads/2018/03/IOBO-Humpy-Natural-Dun.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Galloup’s Compara Spinner – Variation", "https://www.johnkreft.com/wp-content/uploads/2017/09/Galloups-Compara-Spinner.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Stalcup’s CDC Biot Comparadun", "https://www.johnkreft.com/wp-content/uploads/2019/02/Stalcups-CDC-Biot-Comparadun-1024x749.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("Stalcup’s Cripple Emerger", "https://www.johnkreft.com/wp-content/uploads/2019/02/Stalcups-Cripple-Emerger-1024x727.jpg", "Dry", "Mayfly", "Emerger")
        Flies.create("Stalcup’s Emerging Dun", "https://www.johnkreft.com/wp-content/uploads/2019/02/Stalcups-Emerging-Dun-1024x697.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("Starling and Purple", "https://www.johnkreft.com/wp-content/uploads/2018/10/Starling-and-Purple-Soft-Hackle.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Almost There Baetis", "https://www.johnkreft.com/wp-content/uploads/2020/04/Almost-There-Baetis-Olive.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("Galloup’s Sunken Spinner", "https://www.johnkreft.com/wp-content/uploads/2020/04/Galloups-Sunken-Spinner-Top-View.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("Galloup’s Compara Spinner", "https://www.johnkreft.com/wp-content/uploads/Galloups-Compara-Spinner-Dubbed-Body-1024x683.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Film Critic March Brown", "https://www.johnkreft.com/wp-content/uploads/Film-Critic-March-Brown.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Light Hendrickson", "https://www.johnkreft.com/wp-content/uploads/Light-Hendrickson.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("Dark Hendrickson", "https://www.johnkreft.com/wp-content/uploads/Dark-Hendrickson.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("Flick’s March Brown", "https://www.johnkreft.com/wp-content/uploads/Flicks-March-Brown.jpg", "Dry", "Mayfly", "Adult")
        Flies.create("Stalcup’s CDC Emerging Dun", "https://www.johnkreft.com/wp-content/uploads/Stalcups-CDC-Emerging-Dun-March-Brown.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("RiverKeeper Beta Spinner", "https://www.johnkreft.com/wp-content/uploads/RiverKeeper-Beta-Spinner-1.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Lively’s March Brown", "https://www.johnkreft.com/wp-content/uploads/Livelys-March-Brown-Dun.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Clark’s Big Mayfly", "https://www.johnkreft.com/wp-content/uploads/Clarks-Big-Olive-Mayfly.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Mel’s McKenzie Mayfly", "https://www.johnkreft.com/wp-content/uploads/2014/03/Mels-McKenzie-Mayfly-1024x586.jpg.webp", "Dry", "Mayfly", "Adult")
        Flies.create("Baetis Soft Hackle", "https://www.johnkreft.com/wp-content/uploads/Baetis-Soft-Hackle.jpg", "Wet", "Mayfly", "Nymph")
        Flies.create("BWO Pulsating Emerger", "https://www.johnkreft.com/wp-content/uploads/BWO-Pulsating-Emerger-Close-up.jpg", "Wet", "Mayfly", "Emerger")
        Flies.create("$3 Dip", "https://www.johnkreft.com/wp-content/uploads/2018/01/3-Dip-Gold-Bead.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Bling", "https://www.johnkreft.com/wp-content/uploads/2015/03/Bling.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Barber Pole Perdigon", "https://www.johnkreft.com/wp-content/uploads/2018/01/Barber-Pole-Perdigon.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Bird’s Nest Nymph", "https://www.johnkreft.com/wp-content/uploads/2018/03/Birds-Nest-Natural-with-Bead-Head.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Copper John Nymph", "https://www.johnkreft.com/wp-content/uploads/2014/08/Copper-John-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Egan’s Red Dart", "https://www.johnkreft.com/wp-content/uploads/2020/01/Egans-Red-Dart.jpg.webp", "Wet", "Mayfly" ,"Nymph")
        Flies.create("Frenchie", "https://www.johnkreft.com/wp-content/uploads/2014/12/Frenchie-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Hare Ear Nymph", "https://www.johnkreft.com/wp-content/uploads/2014/08/Hares-Ear-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Good and Plenty", "https://www.johnkreft.com/wp-content/uploads/2015/02/Good-and-Plenty.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Krystal Flash Nymph", "https://www.johnkreft.com/wp-content/uploads/2017/07/Krystal-Flash-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Higas SOS", "https://www.johnkreft.com/wp-content/uploads/2018/11/Higas-SOS.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Lightning Bug", "https://www.johnkreft.com/wp-content/uploads/2016/01/Lighning-Bug.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Lights Out", "https://www.johnkreft.com/wp-content/uploads/2015/08/Lights-Out4.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Mercers Poxyback Green Drake Nymph", "https://www.johnkreft.com/wp-content/uploads/2015/04/Mercers-Poxyback-Green-Drake-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Olive Perdigon", "https://www.johnkreft.com/wp-content/uploads/2019/02/Olive-Perdigon.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Peacock Nymph", "https://www.johnkreft.com/wp-content/uploads/2015/01/Peacock-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Partridge and Orange", "https://www.johnkreft.com/wp-content/uploads/2020/03/Partridge-and-Orange.jpg", "Wet", "Mayfly", "Nymph")
        Flies.create("Bead Head Pheasant Tail", "https://www.johnkreft.com/wp-content/uploads/2019/02/Bead-Head-Pheasant-Tail-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Pheasant Tail Soft Hackle", "https://www.johnkreft.com/wp-content/uploads/2020/03/Pheasant-Tail-Soft-Hackle.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Pheasant Tail Perdigon", "https://www.johnkreft.com/wp-content/uploads/2019/02/Pheasant-Tail-Perdigon-Variant.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Pheasant Tail Perdigon – Seitz Version", "https://www.johnkreft.com/wp-content/uploads/2018/01/Pheasant-Tail-Perdigon.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Pliva Perdigon", "https://www.johnkreft.com/wp-content/uploads/2018/01/Pliva-Perdigon.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Prince Nymph", "https://www.johnkreft.com/wp-content/uploads/2018/10/Prince-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Rainbow Warrior", "https://www.johnkreft.com/wp-content/uploads/2018/01/Rainbow-Warrior-1.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Rainbow Warrior Perdigon", "https://www.johnkreft.com/wp-content/uploads/2019/02/Rainbow-Warrior-Perdigon.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Root Beer Float Perdigon", "https://www.johnkreft.com/wp-content/uploads/2018/01/Root-Beer-Float-Perdigon.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Skip Nymph", "https://www.johnkreft.com/wp-content/uploads/2015/04/Skip-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("SLS Soft Hackle Emerger", "https://www.johnkreft.com/wp-content/uploads/2017/01/SLF-Soft-Hackle-Emerger.jpg.webp", "Wet", "Mayfly", "Emerger")
        Flies.create("WD-40", "https://www.johnkreft.com/wp-content/uploads/2018/11/WD-40.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("WK Thread Body Mayfly Nymph", "https://www.johnkreft.com/wp-content/uploads/2015/01/WK-Thread-Body-Mayfly-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Flick’s March Brown Nymph", "https://www.johnkreft.com/wp-content/uploads/Flicks-March-Brown-Nymph.jpg.webp", "Wet", "Mayfly", "Nymph")
        Flies.create("Wollum’s Brown Drake Emerger", "https://www.johnkreft.com/wp-content/uploads/Brown-Drake-Emerger.jpg.webp", "Wet", "Mayfly", "Emerger")
        Flies.create("X Caddis", "https://www.johnkreft.com/wp-content/uploads/2018/03/X-Caddis-Tan.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("Improved F Fly", "https://www.johnkreft.com/wp-content/uploads/2019/07/Improved-F-Fly.jpg", "Dry", "Caddis", "Adult")
        Flies.create("Iris Caddis", "https://www.johnkreft.com/wp-content/uploads/2016/09/Iris-Caddis-Tan.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("Amber Caddis Klinkhåmer Variant", "https://www.johnkreft.com/wp-content/uploads/2017/10/Amber-Caddis-Klinkhamer-Variant.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("Bead Head Soft Hackle", "https://www.johnkreft.com/wp-content/uploads/2017/05/BH-Soft-Hackle-Olive.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Bird’s Nest Nymph Caddis", "https://www.johnkreft.com/wp-content/uploads/2018/03/Birds-Nest-Natural-with-Bead-Head.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("CDC Bubble Caddis", "https://www.johnkreft.com/wp-content/uploads/2017/03/McPhail-CDC-Bubble-Caddis-Closeup.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("CDC & Elk", "https://www.johnkreft.com/wp-content/uploads/2014/07/CDC-Elk.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("Crystal Serendipity", "https://www.johnkreft.com/wp-content/uploads/2018/03/Crystal-Dip.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Elk Hair Caddis", "https://www.johnkreft.com/wp-content/uploads/2018/10/Elk-Hair-Caddis.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("Caddis Euro Nymph", "https://www.johnkreft.com/wp-content/uploads/2015/04/Euro-Jig-Nymph-Tan.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Glossosoma Caddis Larva", "https://www.johnkreft.com/wp-content/uploads/2016/07/Glossosoma-Caddis-Larva.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Hemingway Caddis", "https://www.johnkreft.com/wp-content/uploads/2020/11/Hemingway-Caddis-Olive.jpg", "Dry", "Caddis", "Adult")
        Flies.create("Kings River Caddis", "https://www.johnkreft.com/wp-content/uploads/2017/05/King-River-Caddis.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("Klinkhåmer Special", "https://www.johnkreft.com/wp-content/uploads/2017/09/Klinkhamer-Special.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("LaFontaine Diving Caddis", "https://www.johnkreft.com/wp-content/uploads/2015/10/LaFontaine-Diving-Caddis.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("LaFontaine Emergent Sparkle Pupa", "https://www.johnkreft.com/wp-content/uploads/2017/04/LaFontaine-Emergent-Sparkle-Pupa-Green.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("LaFontaine Sparkle Pupa", "https://www.johnkreft.com/wp-content/uploads/2015/04/LaFontaine-Sparkle-Pupa.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("McKenzie Caddis – Dry", "https://www.johnkreft.com/wp-content/uploads/2017/03/McKenzie-Caddis-Dry-Fly.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("McKenzie Caddis Wet Fly", "https://www.johnkreft.com/wp-content/uploads/2017/03/McKenzie-Caddis-Wet-Fly.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Mercer’s Missing Link", "https://www.johnkreft.com/wp-content/uploads/2015/09/Mercers-Missing-Link.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("Mercury Cased Caddis", "https://www.johnkreft.com/wp-content/uploads/2015/02/Mercury-Cased-Caddis.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Miasmic October Caddis Pupa-Emerger", "https://www.johnkreft.com/wp-content/uploads/2019/09/Miasmic-October-Caddis-Pupa-Emerger.jpg", "Wet", "Caddis", "Emerger")
        Flies.create("Morrish Deep October Caddis", "https://www.johnkreft.com/wp-content/uploads/2017/08/Morrish-Deep-October-Caddis-Pupa-Variant.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Morris October Caddis", "https://www.johnkreft.com/wp-content/uploads/2016/10/Morrish-October-Caddis.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("Peacock Caddis", "https://www.johnkreft.com/wp-content/uploads/2015/04/Peacock-Caddis.jpg.webp", "Dry", "Caddis", "Adult")
        Flies.create("Silvey’s Caddis Pupa", "https://www.johnkreft.com/wp-content/uploads/Silveys-Caddis-Pupa-Tan.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Electric Caddis", "https://www.johnkreft.com/wp-content/uploads/Electric-Caddis.jpg", "Wet", "Caddis", "Nymph")
        Flies.create("Caddistrophic Caddis", "https://www.johnkreft.com/wp-content/uploads/Caddistrophic-Caddis-Olive-1.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Peeking Caddis", "https://www.johnkreft.com/wp-content/uploads/Peeking-Caddis.jpg.webp", "Wet", "Caddis", "Nymph")
        Flies.create("Clark’s Golden Stone", "https://www.johnkreft.com/wp-content/uploads/2019/02/Clarks-Golden-Stone.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Clark’s Lady Golden Stone", "https://www.johnkreft.com/wp-content/uploads/2019/05/Clarks-Lady-Stone.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Clark’s Salmonfly", "https://www.johnkreft.com/wp-content/uploads/2020/05/Clarks-Stone-Salmonfly.jpg", "Dry", "Stonefly", "Adult")
        Flies.create("Clark’s Lady Salmonfly", "https://www.johnkreft.com/wp-content/uploads/2020/05/Clarks-Lady-Stone-Salmonfly.jpg", "Dry", "Stonefly", "Adult")
        Flies.create("Clark’s Lady Stone – Skwala", "https://www.johnkreft.com/wp-content/uploads/2020/03/Clarks-Lady-Stone-Skwala-with-Natural-Colored-Olive-Tail.jpg", "Dry", "Stonefly", "Adult")
        Flies.create("Norm Wood Special", "https://www.johnkreft.com/wp-content/uploads/2020/01/Norm-Wood-Special.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Chernobyl Ant Black & Tan", "https://www.johnkreft.com/wp-content/uploads/2020/05/Chernobyl-Ant-Black-Tan.jpg", "Dry", "Stonefly", "Adult")
        Flies.create("Chubby Chernobyl – Golden Stone", "https://www.johnkreft.com/wp-content/uploads/Chubby-Chernobyl-Golden-Stone.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Fat Albert", "https://www.johnkreft.com/wp-content/uploads/2016/03/Fat-Albert.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Kaufmann’s Stimulator Salmonfly", "https://www.johnkreft.com/wp-content/uploads/2014/05/Kaufmanns-Salmonfly-Stimulator-1024x768.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Kaufmann’s Stimulator Golden Stone", "https://www.johnkreft.com/wp-content/uploads/2015/01/Kaufmanns-Stimulator-Golden-Stone.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Langtry Special", "https://www.johnkreft.com/wp-content/uploads/2017/06/Langtry-Special.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Patient Angler Stone", "https://www.johnkreft.com/wp-content/uploads/2017/06/Patient-Angler-Stone-1.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Plan B – Purple", "https://www.johnkreft.com/wp-content/uploads/2020/05/Plan-B-Purple.jpg", "Dry", "Stonefly", "Adult")
        Flies.create("Rogue Foam Stone", "https://www.johnkreft.com/wp-content/uploads/2016/03/Rogue-Foam-Stonefly.jpg.webp", "Dry", "Stonefly", "Adult ")
        Flies.create("Royal Stimulator", "https://www.johnkreft.com/wp-content/uploads/Royal-Stimulator-2.jpg", "Dry", "Stonefly", "Adult")
        Flies.create("Skwala 1", "https://www.johnkreft.com/wp-content/uploads/2014/03/Skwala-1.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Skwala #2", "https://www.johnkreft.com/wp-content/uploads/2020/05/Skwala-2.jpg", "Dry", "Stonefly", "Adult")
        Flies.create("Doculator", "https://www.johnkreft.com/wp-content/uploads/Doculator-Yellow-16.jpg.webp", "Dry", "Stonefly", "Adult")
        Flies.create("Bird’s Nest Nymph", "https://www.johnkreft.com/wp-content/uploads/2018/03/Birds-Nest-Natural-with-Bead-Head.jpg.webp", "Wet", "Stonefly", "Nymph")
        Flies.create("Double Bead Peacock Stone Nymph", "https://www.johnkreft.com/wp-content/uploads/2018/01/Double-Bead-Peacock-Stonefly-Nymph.jpg.webp", "Wet", "Stonefly", "Nymph")
        Flies.create("Jimmy Legs", "https://www.johnkreft.com/wp-content/uploads/2020/05/Jimmy-Legs.jpg", "Wet", "Stonefly", "Nymph")
        Flies.create("Matt’s Fur", "https://www.johnkreft.com/wp-content/uploads/2015/01/Matts-Fur.jpg.webp", "Wet", "Stonefly", "Nymph")
        Flies.create("McPhail’s Golden Stonefly Nymph – Variant", "https://www.johnkreft.com/wp-content/uploads/McPhails-Golden-Stone-Nymph-Variant.jpg.webp", "Wet", "Stonefly", "Nymph")
        Flies.create("Pat’s Rubberlegs", "https://www.johnkreft.com/wp-content/uploads/2016/07/Pats-Rubberlegs.jpg.webp", "Wet", "Stonefly", "Nymph")
        Flies.create("RiverKeeper Stonefly Nymph", "https://www.johnkreft.com/wp-content/uploads/2016/03/RiverKeeper-Stonefly-Nymph.jpg.webp", "Wet", "Stonefly", "Nymph")
        Flies.create("Bitch Creek Nymph", "https://www.johnkreft.com/wp-content/uploads/2019/10/Bitch-Creek-Nymph.jpg.webp", "Wet", "Stonefly", "Nymph")
        Flies.create("Kaufmann’s Simulator Peacock", "https://www.johnkreft.com/wp-content/uploads/Kaufmanns-Simulator-Peacock.jpg.webp", "Wet", "Stonefly", "Nymph")
        Flies.create("Biot Backed Stonefly", "https://www.johnkreft.com/wp-content/uploads/Biot-Backed-Stonefly.jpg.webp", "Wet", "Stonefly", "Nymph")
        Flies.create("Beetle Bailey", "https://www.johnkreft.com/wp-content/uploads/2017/09/Beetle-Bailey.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Beetle Betty", "https://www.johnkreft.com/wp-content/uploads/2014/07/Beetle-Betty-1024x693.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Simple Beetle", "https://www.johnkreft.com/wp-content/uploads/2019/06/Simple-Beetle.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Arrick’s Parachute Ant", "https://www.johnkreft.com/wp-content/uploads/2018/09/Arricks-Parachute-Ant.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Galloup’s Ant Acid", "https://www.johnkreft.com/wp-content/uploads/2018/09/Galloups-Ant-Acid.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Harrop’s CDC Ant (Cinnamon)", "https://www.johnkreft.com/wp-content/uploads/2018/09/Harrops-CDC-Ant-Cinnamon.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Harrop’s CDC Ant (Black)", "https://www.johnkreft.com/wp-content/uploads/2018/09/Harrops-CDC-Ant-Black.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Chernobyl Ant Black & Tan", "https://www.johnkreft.com/wp-content/uploads/2020/05/Chernobyl-Ant-Black-Tan.jpg", "Dry", "Terrestrial", "Adult")
        Flies.create("Chernobyl Ant Black & Red", "https://www.johnkreft.com/wp-content/uploads/2020/05/Chernobyl-Ant-Black-Red.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Improved Chaos Hopper", "https://www.johnkreft.com/wp-content/uploads/2018/09/Chaos-Hopper.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Schroeder’s Parachute Hopper", "https://www.johnkreft.com/wp-content/uploads/Schroeders-Hopper.jpg", "Dry", "Terrestrial", "Adult")
        Flies.create("Fat Albert", "https://www.johnkreft.com/wp-content/uploads/2016/03/Fat-Albert.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Thunder Thighs Hopper", "https://www.johnkreft.com/wp-content/uploads/2020/04/Thunder-Thighs-Tan.jpg", "Dry", "Terrestrial", "Adult")
        Flies.create("Dave’s Hopper", "https://www.johnkreft.com/wp-content/uploads/Daves-Hopper.jpg", "Dry", "Terrestrial", "Adult")
        Flies.create("Card’s Cicada", "https://www.johnkreft.com/wp-content/uploads/Cards-Cicada.jpg.webp", "Dry", "Terrestrial", "Adult")
        Flies.create("Swisher’s PMX Royal", "https://www.johnkreft.com/wp-content/uploads/Swishers-PMX-Royal.jpg", "Dry", "Terrestrial", "Adult")
        Flies.create("Dolly Llama", "https://www.johnkreft.com/wp-content/uploads/2016/11/Dolly-Llama.jpg.webp", "Streamer", "Baitfish", "Adult")
        Flies.create("Pheasant Rump Muddler", "https://www.johnkreft.com/wp-content/uploads/2020/04/Pheasant-Rump-Muddler.jpg", "Streamer", "Baitfish", "Adult")
        Flies.create("Barr’s Meat Whistle", "https://www.johnkreft.com/wp-content/uploads/2020/06/Barrs-Meat-Whistle.jpg", "Streamer", "Baitfish", "Adult")
        Flies.create("EP Bait Fish", "https://www.johnkreft.com/wp-content/uploads/EP-Bait-Fish.jpg", "Streamer", "Baitfish", "Adult")
        Flies.create("Double Bunny", "https://www.johnkreft.com/wp-content/uploads/Double-Bunny.jpg", "Streamer", "Baitfish", "Adult")
        Flies.create("Blonde Goddess", "https://www.johnkreft.com/wp-content/uploads/Blonde-Goddess.jpg", "Streamer", "Baitfish", "Adult")
        Flies.create("Bouface Streamer", "https://www.johnkreft.com/wp-content/uploads/Bouface-Streamer.jpg", "Streamer", "Baitfish", "Adult")
        Flies.create("Thunder Creek Streamer – Sockeye Fry", "https://www.johnkreft.com/wp-content/uploads/Thunder-Creek-Streamer-Sockeye.jpg", "Streamer", "Baitfish", "Adult")
        Flies.create("$3 Dip", "https://www.johnkreft.com/wp-content/uploads/2018/01/3-Dip-Gold-Bead.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("California Mosquito", "https://www.johnkreft.com/wp-content/uploads/2020/08/California-Mosquito.jpg", "Dry", "Midge", "Adult")
        Flies.create("Crystal Serendipity", "https://www.johnkreft.com/wp-content/uploads/2018/03/Crystal-Dip.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("Deep Blue Poison Tung", "https://www.johnkreft.com/wp-content/uploads/2015/02/Deep-Blue-Poison-Tung.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("Diving Egg Laying Midge", "https://www.johnkreft.com/wp-content/uploads/2019/01/LaFontaines-Diving-Egg-Laying-Midge.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("East Lake Chironomid", "https://www.johnkreft.com/wp-content/uploads/2016/02/East-Lake-Chironomid.jpg", "Wet", "Midge", "Nymph")
        Flies.create("Engle’s Micro Soft-Hackle", "https://www.johnkreft.com/wp-content/uploads/2018/12/Engles-Micro-Soft-Hackle.jpg.webp", "Dry", "Midge", "Adult")
        Flies.create("Grey Ugly", "https://www.johnkreft.com/wp-content/uploads/2020/09/Grey-Ugly.jpg", "Dry", "Midge", "Adult")
        Flies.create("Griffiths Gnat", "https://www.johnkreft.com/wp-content/uploads/2020/09/Griffiths-Gnat.jpg", "Dry", "Midge", "Adult")
        Flies.create("Griffith’s Gnat Emerger", "https://www.johnkreft.com/wp-content/uploads/2018/10/Griffiths-Gnat-Emerger.jpg.webp", "Dry", "Midge", "Emerger")
        Flies.create("Half Pint Midge", "https://www.johnkreft.com/wp-content/uploads/2016/03/Half-Pint-Midge.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("Higas SOS", "https://www.johnkreft.com/wp-content/uploads/2018/11/Higas-SOS-with-UV-Resin.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("Harrop’s CDC Transitional Midge", "https://www.johnkreft.com/wp-content/uploads/2017/11/Harrops-CDC-Midge-Emerger.jpg.webp", "Dry", "Midge", "Emerger")
        Flies.create("In-The-Film CDC Emerger", "https://www.johnkreft.com/wp-content/uploads/2020/11/In-The-Film-CDC-Midge-Emerger-Black.jpg.webp", "Dry", "Midge", "Emerger")
        Flies.create("Matt’s Midge", "https://www.johnkreft.com/wp-content/uploads/2016/11/Matts-Midge.jpg.webp", "Dry", "Midge", "Adult")
        Flies.create("Micro Madison Midge", "https://www.johnkreft.com/wp-content/uploads/2015/11/Micro-Madison-Midge-Pearl.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("Mighty Midget Emerger", "https://www.johnkreft.com/wp-content/uploads/2017/04/Mighty-Midget-Emerger.jpg.webp", "Dry", "Midge", "Emerger")
        Flies.create("Mercury Midge", "https://www.johnkreft.com/wp-content/uploads/2018/10/Mercury-Midge.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("Miracle Midge", "https://www.johnkreft.com/wp-content/uploads/2015/02/Miracle-Midge-Wet.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("OB2Wanchironomie", "https://www.johnkreft.com/wp-content/uploads/2020/04/OB2Wanchironomie.jpg", "Wet", "Midge", "Nymph")
        Flies.create("Peg’s Midge", "https://www.johnkreft.com/wp-content/uploads/2016/11/Pegs-Midge.jpg.webp", "Dry", "Midge", "Adult")
        Flies.create("Roy’s Special Emerger", "https://www.johnkreft.com/wp-content/uploads/Roys-Special-Emerger.jpg", "Dry", "Midge", "Emerger")
        Flies.create("Scotty’s Midge", "https://www.johnkreft.com/wp-content/uploads/2017/04/Scottys-Midge.jpg.webp", "Dry", "Midge", "Adult")
        Flies.create("Stuck-In-The-Shuck Midge", "https://www.johnkreft.com/wp-content/uploads/Stuck-In-The-Shuck-Midge.jpg", "Dry", "Midge", "Adult")
        Flies.create("WD-40", "https://www.johnkreft.com/wp-content/uploads/2018/11/WD-40.jpg.webp", "Wet", "Midge", "Nymph")
        Flies.create("Zebra Midge", "https://www.johnkreft.com/wp-content/uploads/2020/12/Zebra-Midge-Black.jpg", "Wet", "Midge", "Nymph")
        Flies.create("Zelon Midge", "https://www.johnkreft.com/wp-content/uploads/Zelon-Midge-Olive-Dun-Body.jpg.webp", "Dry", "Midge", "Adult")
        Flies.create("Manhattan Midge", "https://www.johnkreft.com/wp-content/uploads/Manhattan-Midge.jpg", "Wet", "Midge", "Nymph")
        Flies.create("Black Beauty Midge", "https://www.johnkreft.com/wp-content/uploads/Black-Beauty-Midge-Daiichi-1100-22.jpg", "Wet", "Midge", "Nymph")
        Flies.create("Mercury Black Beauty", "https://www.johnkreft.com/wp-content/uploads/Mercury-Black-Beauty-Daiichi-1100-22.jpg", "Wet", "Midge", "Nymph")


        print("Database seeded successfully!")

    except Exception as e:
        print("Error occurred during database seeding:", e)

if __name__ == "__main__":
    seed_database()