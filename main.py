from clases.class_humano import Humano
from clases.class_elfo import Elfo
from clases.class_enano import Enano
from clases.class_gnomo import Gnomo
from clases.class_mediano import Mediano
from clases.class_semielfo import Semielfo
from clases.class_semiorco import Semiorco

if __name__ == "__main__":
    Porongo = Humano('Porongo','Masculino')
    Porongo.show_all_stats()
    print('\n')
    Jorge = Elfo('Jorge','Masculino')
    Jorge.show_all_stats()
    print('\n')
    Maxi = Enano('Maxi','Masculino')
    Maxi.show_all_stats()
    print('\n')
    Gabo = Mediano('Gabo','Masculino')
    Gabo.show_all_stats()
    print('\n')
    John = Gnomo('John','Masculino')
    John.show_all_stats()
    print('\n')
    Niz = Semielfo('Niz','Masculino')
    Niz.show_all_stats()
    print('\n')
    Nico = Semiorco('Nico','Masculino')
    Nico.show_all_stats()