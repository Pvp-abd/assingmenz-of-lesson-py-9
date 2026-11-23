

class ArtGallery:
    def __init__(self, gallery_name, city):
        
        self.gallery_name, self.city = "Untitled", "?" 
        self.artworks = ["(no artworks: write TODO 1)"]  

    def add_artwork(self, title):
       
        print("add_artwork is not written yet") 

    def remove_artwork(self, title):
      
        print("remove_artwork is not written yet") 

    def show(self):                                            
        print(f"{self.gallery_name}, artworks: {len(self.artworks)}", self.artworks)

 


gallery = ArtGallery("Little Brushes Gallery", "Portland")       
while True:                                                    
    choice = input("\n1. Add  2. Remove  3. Show  4. Close\nChoice: ").strip()
    if choice == "1":
        gallery.add_artwork(input("Title: ").strip())
    elif choice == "2":
        gallery.remove_artwork(input("Title to remove: ").strip())
    elif choice == "3":
        gallery.show()
    elif choice == "4":
        del gallery
        break
    else:
        print("Please type 1, 2, 3 or 4.")
