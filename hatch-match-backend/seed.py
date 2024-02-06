#!/usr/bin/env python3

from DB.__init__ import CONN, CURSOR
from DB.flies import Flies
from DB.fly_type import Fly_type
from DB.species import Species

def seed_database():
    try:
        Fly_type.drop_table()
        Fly_type.create_table()

        Flies.drop_table()
        Flies.create_table()

        Species.drop_table()
        Species.create_table()

        Trout = Species.create("Trout", "https://content.osgnetworks.tv/flyfisherman/content/photos/AboutRainbowTrout-HERO-1200x800.jpg")
        Panfish = Species.create("Panfish", "https://www.panthermartin.com/img/FishSpecies/sm/15_Panfish.jpg")
        Bass = Species.create("Bass", "https://www.maine.gov/ifw/images/largemouth-bass600.jpg")

        Dry_fly = Fly_type.create("Dry Fly")
        Wet_fly = Fly_type.create("Wet Fly")
        Nymph = Fly_type.create("Nymph")
        Emerger = Fly_type.create("Emerger")

        Flies.create("Adams", "https://content.osgnetworks.tv/flyfisherman/content/photos/TweakingAdams2-1200x800.jpg", Dry_fly.id, Trout.id)
        Flies.create("Bivisible", "https://flyfishingthesierra.com/images/bivis/bivis.jpg", Dry_fly.id, Trout.id)
        Flies.create("Chernobyl Ant", "https://www.flytyer.com/wp-content/uploads/2021/09/Screen-Shot-2021-09-28-at-2.59.03-PM.png", Dry_fly.id, Trout.id)
        Flies.create("Elk hair Caddis", "https://upload.wikimedia.org/wikipedia/commons/0/06/Elk_Hair_Caddis2.jpg", Dry_fly.id, Trout.id)
        Flies.create("F Fly", "https://hawker-overend.com/wp-content/uploads/2021/11/Quill-body-F-flies-final-36K.jpg", Dry_fly.id, Trout.id)
        Flies.create("Fat Albert", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4djDkQnhQ0uuIEoGC7pT2uK_TWAod7PV-mg&usqp=CAU", Dry_fly.id, Bass.id)
        Flies.create("Bluegill Belly Bean", "https://le-cdn.website-editor.net/7d27235173694863ab749a97395fb043/dms3rep/multi/opt/Bonefish+Belly+Bean+12-500w.JPG", Wet_fly.id, Panfish.id)
        Flies.create("Brassie", "https://lh3.googleusercontent.com/proxy/uZsijxT2wqrF_hsx34cY5HNYe1x4_7RA4WuYhjdgUSVgSGaR3fsWDL5QCzTwITxqoTypK2MQbEYIHaWX2I1R-BcKVZdyEiRdeZFo6aauI4hCiTRXEl9n7fASrdHNYWOpty2KNQiiIm8sRw", Wet_fly.id, Trout.id)
        Flies.create("Clouser Minnow", "https://upload.wikimedia.org/wikipedia/commons/8/87/Traditional_Chartreuse_Clouser_Deep_Minnow.jpg", Wet_fly.id, Trout.id)
        Flies.create("Copper John", "https://www.flies-stepbystep.com/wp-content/uploads/2021/01/IMG_7644.jpg", Nymph.id, Trout.id)
        Flies.create("EZ Nymph", "https://www.flytying.guide/media/uploads/1021/0903ca6d-e850-4ff1-8f54-e8b6ad0e16c0.jpg?width=800", Nymph.id, Trout.id)
        Flies.create("Fire Scud", "https://www.crosscurrents.com/wp-content/uploads/2018/01/Firebead-Caviar-Scud-orange.jpg", Nymph.id, Trout.id)
        Flies.create("Elk Hair Emerger", "https://i.ytimg.com/vi/3ABafzWjFDU/hqdefault.jpg", Emerger.id, Trout.id)
        Flies.create("March Brown Emerger", "https://west-branch-angler.myshopify.com/cdn/shop/products/unspecified_32_1024x1024.jpg?v=1479072500", Emerger.id, Trout.id)
        print("Database seeded successfully!")

    except Exception as e:
        print("Error occurred during database seeding:", e)

if __name__ == "__main__":
    seed_database()
