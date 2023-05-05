import random


class Libro:
    def __init__(self, isbn, title, genre=0, idiom=0, cost=0):
        self.codigo = isbn
        self.titulo = title
        self.genero = genre
        self.idioma = idiom
        self.costo = cost


def menu():
    print('{:^40}'.format(chr(27) + "[1;93;m" + "MENÚ DE OPCIONES" + chr(27) + "[0m"))
    print(chr(27) + "[34m" + "1-Carga manual de libros" + chr(27) + "[0m")
    print(chr(27) + "[34m" + "2-Carga automática de libros" + chr(27) + "[0m")
    print(chr(27) + "[34m" + "3-Cantidad por género y el más popular" + chr(27) + "[0m")
    print(chr(27) + "[34m" + "4-Mayor precio en un idioma" + chr(27) + "[0m")
    print(chr(27) + "[34m" + "5-Búsqueda por ISBN" + chr(27) + "[0m")
    print(chr(27) + "[34m" + "6-Mostrar libros del género con más libros" + chr(27) + "[0m")
    print(chr(27) + "[34m" + "7-Consulta de precio por grupo" + chr(27) + "[0m")
    print(chr(27) + "[34m" + "0-Salir" + chr(27) + "[0m")


def generar_code():
    ncode_ok = True
    vuelta = 0
    while ncode_ok:
        vuelta += 1
        code = str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + \
               str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + \
               str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + \
               str(random.randint(1, 9))
        if vuelta > 1:
            ncode = int(code[0]) * 10 + int(code[1]) * 9 + int(code[2]) * 8 + int(code[3]) * 7 + int(code[4]) * 6 + \
                int(code[5]) * 5 + int(code[6]) * 4 + int(code[7]) * 3 + int(code[8]) * 2 + int(code[9])
            if ncode % 11 == 0:
                return code


def generar_isbn():
    code_ok = False
    while not code_ok:
        code_ok = True
        code = generar_code()
        isbn = []
        for i in code:
            isbn.append(i)
        for i in range(3):
            isbn.insert(random.randint(1, 8), '-')
        g1 = False
        for i in isbn:
            if i != '-':
                g1 = False
            if i == '-' and g1:
                code_ok = False
            if i == '-':
                g1 = True

    isbnx = ''.join(isbn)
    return isbnx


def generar_titulo():
    titulos = ['Poema de Gilgamesh', 'El libro de Job', 'Biblia', 'Las mil y una noches', 'Saga de Njál', 'La cigarra',
               'Todo se desmorona', '100 cuentos infantiles', 'Divina comedia', 'Orgullo y prejuicio', 'Escuela física',
               'Papá Goriot', 'El Innombrable', 'Decamerón', 'Cumbres Borrascosas', 'El extranjero', 'El gran arcoiris',
               'Viaje al fin de la noche', 'Don Quijote de la Mancha', 'Los cuentos de Canterbury', 'ÉL y Mary',
               'Relatos cortos', 'Nostromo', 'Grandes esperanzas', 'Berlin Alexanderplatz', 'Crimen y castigo', 'Rocas',
               'Jacques el fatalista', 'Los hermanos Karamazov', 'El idiota', 'Los endemoniados', 'Middlemarch',
               'Midsommermort', '¡Absalom, Absalom!', 'Ruido y furia', 'El hombre invisible', 'Medea', 'Tú puedes',
               'Madame Bovary', 'Educación sentimental', 'Romance gitano', 'Cien años de soledad', 'Almas muertas',
               'Fausto', 'El amor en tiempos de cólera', 'Hambre', 'El viejo y el tambor', 'El mar revuelto', 'Florada',
               '¡No puede ser!', 'Odisea', 'Ulises', 'Zorba, el griego', 'Quién pudiera', 'Yo, me quiero', 'Libre',
               'Libremente libre', 'Libertad, libertad, libertad!', 'Diario de un loco', 'Mis hijos', 'Me da sueño',
               'Por favor, llévensela!', '70 años de decadencia', 'El cuaderno dorado', 'Moby-dick', 'Te encontraré!',
               'En busca del tiempo perdido', 'Dime que me amas', 'La soledad', 'Ésto es el amor?', '1984', 'Lolita',
               'La metamorfósis', 'El científico y su estilo', 'Leon', 'Leonard', 'Leopold', 'Leroy', 'Lester', 'Levi',
               'Lewis', 'Lincoln', 'Lindwood', 'Lionel', 'Lloyd', 'Louis', 'Lucas', 'Lucian', 'Luke', 'Luther', 'Mack',
               'Madison', 'Major', 'Malachi', 'Edipo rey', 'Rojo y negro', 'EL sol nasciente', 'Ser', 'La llamada',
               'La cosa', 'Ultratumba', 'Un asesinato sin presedente', 'No quiero morir así', 'Pecho a las balas',
               'La salud mental', 'La liquidez en la sociedad', 'Memorias de un viejo', 'Los herederos de Alberdi',
               'Avigail', 'Avital', 'Aviva', 'Aya', 'Ayala', 'Ayla', 'Aziza', 'Baila', 'Bailey', 'Barbara', 'El calcio',
               'Barbary', 'Barbery', 'Barbi', 'Barbie', 'Basya', 'Bathsheba', 'Batsheva', 'Beatrice', 'Beatrix',
               'Becca', 'Becky', 'Belinda', 'Bell', 'Bella', 'Belle', 'Bernadette', 'Bernice', 'Bertha', 'Beryl',
               'Bessie', 'Beth', 'Bethany', 'Bethena', 'Bethia', 'Betsey', 'Betsy', 'Bette', 'Betty', 'Beulah',
               'Beverly', 'Bianca', 'Biddy', 'Billie', 'Binky', 'Binny', 'Bisky', 'Bitsy', 'Blair', 'Blake', 'La rosa'
               'Blanca', 'Blanche', 'Bleba', 'Blima', 'Blimy', 'Bliss', 'Bonnibel', 'Bonnie', 'Boone', 'Bracha',
               'Brandi', 'Brandy', 'Breanna', 'Bree', 'Breindy', 'Brenda', 'Briana', 'Brianna', 'Bridges', 'El sol'
               'Bridget', 'Brielle', 'Brilliana', 'Britannia', 'Britney', 'Brittany', 'Brittney', 'Bronwyn',
               'Brooke', 'Brooklyn', 'Brucha', 'Bruchy', 'Brunhild', 'Bryanne', 'Brynn', 'Buffy', 'Bunny', 'Cerveza'
               'Cadence', 'Caitlin', 'Calista', 'Callie', 'Camellia', 'Cameron', 'Camila', 'Camilla', 'Camille',
               'Candice', 'Carla', 'Carlene', 'Carly', 'Carol', 'Carole', 'Carolina', 'Caroline', 'Carolyn', 'Probable',
               'Carrie', 'Casey', 'Cassandra', 'Cassidy', 'Catalina', 'Cate', 'Cath', 'Catharine', 'Catherine',
               'Cathern', 'Cathy', 'Cayce', 'Cecelia', 'Cecila', 'Cecilia', 'Cecily', 'Celene', 'Celeste', 'Talvez',
               'Celestia', 'Celestine', 'Celia', 'Celinda', 'Celine', 'Chana', 'Chanie', 'Chantelle', 'Chany',
               'Charity', 'Charlie', 'Charlott', 'Charlotte', 'Chava', 'Chavy', 'Chaya', 'Chel', 'Chelsea', 'Cercano',
               'Cherry', 'Cheryl', 'Cheyenne', 'Chiara', 'Chloe', 'Chris', 'Christian', 'Christiana', 'El adn negro',
               'Christina', 'La luna y el lobo', 'Las 1000 especies en extinsión', 'Paisajes remotos', 'viaje en moto',
               'Christine', 'Christy', 'Cicely', 'Ciel', 'Cinderella', 'Cindy Lou', 'Cindy', 'Clair', 'Claire',
               'Clara', 'Clare', 'Clarence', 'Clarinda', 'Clarissa', 'Claudia', 'Clayre', 'Clemency', 'Podremos ganar',
               'Clementine', 'Clover', 'Colette', 'Colleen', 'Columbia', 'Comfort', 'Connie', 'Constance', 'Primordial',
               'Constanta', 'Cora', 'Coraline', 'Cordelia', 'Cornelia', 'Courtney', 'Cressida', 'Crimson', 'Evolución'
               'Crispina', 'Crystal', 'Cyntha', 'Cynthia', 'Dahlia', 'Daisy', 'Dalia', 'Dana', 'Daniela', 'Código vega',
               'Daniella', 'Danielle', 'Danna', 'Daphne', 'Darcus', 'Daria', 'Darla', 'Darleen', 'Darlene', 'El mate',
               'Davina', 'Dawn', 'Deanie', 'Debbie', 'Deborah', 'Debra', 'Dee', 'Delia', 'Delila', 'Delilah', 'Raro',
               'Della', 'Delores', 'Delphine', 'Delsie', 'Denise', 'Denyse', 'Desire', 'Destiny', 'Devora', 'Lunático'
               'Devorah', 'Diana', 'Diane', 'Dianne', 'Diantha', 'Dicey', 'Dicy', 'Dina', 'Dinah', 'Dixie', 'Mi tía',
               'Dolly', 'Dolores', 'Donna', 'Dora', 'Dorcas', 'Doreen', 'Doris', 'Dorothea', 'Dorothy', 'Drew',
               'Drusilla', 'Dusty', 'Dylan', 'Easter', 'Ebony', 'Eda', 'Edda', 'Eden', 'Edie', 'Edith', 'Edna',
               'Edney', 'Edwina', 'Effa', 'Effie', 'Eglantine', 'Eileen', 'Elaine', 'Elda', 'Eleanor', 'Electa',
               'Elena', 'Eleni', 'Elenor', 'Eliana', 'Elira', 'Elisa', 'Elisabeth', 'Elise', 'Elisheva', 'Eliz',
               'Eliza', 'Elizabeth', 'Ella', 'Elle', 'Ellen', 'Ellender', 'Ellery', 'Elliana', 'Ellie', 'Ellin',
               'Ellis', 'Elmira', 'Eloise', 'Elsa', 'Elsie', 'Elvira', 'Elyse', 'Elza', 'Emaline', 'Emeline', 'La nona',
               'Emely', 'Emerson', 'Emery', 'Emilia', 'Emiline', 'Emily', 'Emley', 'Emma', 'Emmeline', 'Eneatha',
               'Epa!', 'Erika', 'Erin', 'Ernestine', 'Esme', 'Esmeralda', 'Essie', 'Estella', 'Estelle', 'Las 7 reglas',
               'Ester', 'Su hermana me atrae más', 'Cosas del amor', 'La cocina de la nona', 'Pizzas italianas',
               'Esther', 'Esty', 'Ethel', 'Etta', 'Etty', 'Eudora', 'Eugenia', 'Eugenie', 'Eunice', 'Euphemia',
               'Eva', 'Evaline', 'Evangeline', 'Eve', 'Evelina', 'Eveline', 'Evelyn', 'Everly', 'Evie', 'Imagina-te',
               'Experience', 'Faiga', 'Faigy', 'Faith', 'Fannie', 'Fanny', 'Farah', 'Farmer', 'Fatima', 'Lo quieres?',
               'Felicia', 'Felicity', 'Fidelia', 'Finley', 'Fiona', 'Flannery', 'Flora', 'Florence', 'Florida',
               'Fradel', 'Frady', 'Fraidy', 'France', 'Frances', 'Francesca', 'Fray', 'Frederica', 'Frelove', 'Llámala',
               'Freya', 'Friday', 'Frideswide', 'Frimet', 'Gabriela', 'Gabriella', 'Gabrielle', 'Gage', 'Gaige',
               'Gail', 'Galatia', 'Garnet', 'Gemima', 'Gemma', 'Genevieve', 'Georgia', 'Georgianna', 'Georgina',
               'Geraldine', 'Gertrude', 'Gia', 'Giada', 'Gianna', 'Gillian', 'Gina', 'Ginger', 'Giovanna', 'Uno a uno'
               'Giselle', 'Gittel', 'Gitty', 'Giulia', 'Giuliana', 'Gladis', 'Gladys', 'Glenda', 'Gloria', 'La colina'
               'Yumaná', 'Golda', 'Goldie', 'Goldy', 'Grace', 'Gracie', 'Grayce', 'Grenda', 'Greta', 'Efecto mariposa',
               'Gretchen', '1945', 'Bienvenido a tu peor pesadilla', 'Debería enamorarme de ella', 'Supongo', 'Ciego',
               'Gwen', 'Gwendoline', 'Hadassa', 'Hadassah', 'Hadley', 'Hailey', 'Haley', 'Hana', 'Hanna', 'Mariposa',
               'Hannah', 'Harlow', 'Harmony', 'Harper', 'Harriet', 'Harriette', 'Harriot', 'Hattie', 'Hazel', 'Brasil',
               'Heather', 'Heaven', 'Heidi', 'Helen', 'Helena', 'Hellen', 'Henchy', 'Henny', 'Henrietta', 'Supercolor'
               'Hepsey', 'Hereswith', 'Hermione', 'Hertha', 'Hester', 'Hetta', 'Hilda', 'Hillary', 'Hinda', 'Bariloche',
               'Hindy', 'Holly', 'Honey', 'Honor', 'Honora', 'Huldah', 'Hyacinth', 'Ida', 'Idy', 'Ilana', 'Sub maquina',
               'Imogen', 'India', 'Indiana', 'Ines', 'Ingrid', 'Iona', 'Irene', 'Iris', 'Isabel', 'Isabella',
               'Isabelle', 'Isadore', 'Isla', 'Isolde', 'Issabella', 'Ivy', 'Izabella', 'Jackie', 'Jacqueline',
               'Jacquetta', 'Jada', 'Jade', 'Jamie', 'Jana', 'Jane', 'Janet', 'Janette', 'Janice', 'Janie', 'El diario'
               'Janine', 'La sasmina', 'Jasmine', 'Jaz music', 'Jean', 'Jeann', 'Jeanne', 'Jemima', 'Jemma', 'Jenna',
               'Jennett', 'DJ project', 'La Jennifer', 'Jenny', 'Jerusha', 'Jess', 'Jessamine', 'Jessamy', 'Jessamyn',
               'Wow!', 'Jessica', 'Jessie', 'Jill', 'Jota', 'Joan', 'Joana', 'Joder', 'Joanna', 'Joanne', 'La venganza',
               'Jocelyn', 'Jodie', 'Johanna', 'Jolene', 'Jolie', 'Jones', 'Jordan', 'Jordyn', 'Joselyn', 'Mi favorito',
               'Josephine', 'Joy', 'Joyce', 'Juana', 'Juanita', 'Juda', 'Judith', 'Judy', 'Julia', 'Julian', 'Universo',
               'Juliana', 'Julianna', 'Julie', 'Juliet', 'Juliette', 'June', 'Juniper', 'Justine', 'Kacey', 'Somier',
               'Kaila', 'Kailey', 'Kaitlyn', 'Karen', 'Karin', 'Karol', 'Karoline', 'Kat', 'Kate', 'Katelyn',
               'Katerina', 'Katherine', 'Kathleen', 'Kathryn', 'Kathy', 'Katie', 'Kay', 'Kaya', 'El gran argentino', 
               'El vikingo', 'Los japoneses de la nueva era', 'Oriental y basta', 'Europa y la crisis', 'Para cuándo?',
               'Decíme, Qué es el neoliberalismo?', 'No te entiendo', 'La burla del Papa', 'Ser políglota', 'New York',
               'Nueva era', 'Mi último romance', 'Baby, I am yours', 'The sun', 'Quiero aprender a programar', 'Bye',
               'Every day', 'Hola de nuevo', 'Sé que puedes', 'El sermón', 'Casa de muñecas', 'Tengo miedo', 'Hello',
               'Aprenda a lidiar con el estrés', 'Levántate y pelea', 'Just in case', 'Por las dudas', 'La puerta',
               'Mujer amada', 'El hombre soltero', 'Fuente de luz', 'Matemáticas', 'EL juego perfecto', 'Los dados',
               'Somebody', 'La noche', 'Crudo invierno', 'Feliz primavera', 'Fenómeno monetario', 'La bicicleta',
               'Fantasmas de hace décadas', 'El socialismo y sus fallas', 'No sea progre!', 'Paz eterna de montaña',
               'Sólo un grupo', 'El que labura sólo', 'Cómo ganarle a la pereza?', '¡Haga patria!', 'El soberano',
               'La eterna lucha', 'Diálogo apolítico', 'Soy justo, estoy mal', 'Los inmorales', 'La juventud',
               'Mi cordura pende de un hilo', 'Ser asocial', 'Una mente pobre', 'Curiosamente', 'Brainpower', 'JA!',
               'No me gustan los grupos', 'El tiempo no perdona', 'Una justa causa', 'Felíz Navidad', 'Descanso eterno',
               'El inmortal', 'Bien y mal', 'Post Neurociencia', 'Redes y datos', 'El espacio-tiempo', 'Cosmos',
               'Crónicas de una muerte anunciada', 'La dama y el vagabundo', 'Pinocchio', 'La dama y la bestia',
               'Alicia en el país peronista', 'Aladín', 'La sirenita', 'Robin Hood', 'William Wallace', 'La tribu',
               'Corazón valiente', 'Los aristogatos', 'Jason', 'Deseo un camino', 'En la busqueda de la verdad',
               'Nuevamente intento', 'Qué será de mí?', 'Usted necesita un amigo', 'La amistad', 'El hombre pequeño',
               'La llorona', 'Leyendas de hadas y magos', 'El mito argentino', 'Operación masacre', 'Nuestro girasol',
               'Mi planta de naranja lima', 'El fascismo', 'Marxismo retrogrado', 'Milton Friedman', 'Economía global',
               'Stuart Mill y el feminismo', 'El género y el sexo', 'Python for dummies', 'Machine learning', 'Adiós',
               'No todo es river o boca', 'Fanatismo come cerebros', 'La senda ecléctica', 'Quiero fluir!', 'Gracias',
               'Recetas de la abuela', 'Gourmet francés', 'Puro asado', 'Recetas vegetarianas', 'Salud y comidas',
               'Anastasia', 'Andrea', 'Ange', 'Angela', 'Angelica', 'Angelina', 'Angeline', 'Angie', 'Anisa', 'Locura'
                'Anita', 'Anna', 'Annabel', 'Annabelle', 'Annah', 'Anne', 'Annette', 'Annie', 'Annis', 'Sabueso',
               'El gran robo', 'La casa de papel', 'La anatomía humana', 'Margen de error', 'Día para tomar el té',
               'Estamos aquí', 'Lo que pasa en las estrellas', 'Lo que la gravedad calla', 'De reversaen el tiempo',
               'Las estrellas de mi patio', 'Un paseo al centro de la tierra', 'Eventualmente colapsado', 'Áve fénix',
               'La antigua persia', 'La civilización romana', 'Código civíl', 'Código penal', 'Misterioso Egipto',
               'El electromagnetismo', 'Materia oscura', 'Energía oscura', 'Viaje al cosmos', 'Otra galaxia']

    titulo = random.choice(titulos)
    return titulo.upper()


def mostrar_todo(vector_libros):
    for i in range(len(vector_libros)):
        if vector_libros[i].genero == 0:
            vector_libros[i].genero = 'Autoayuda'
        elif vector_libros[i].genero == 1:
            vector_libros[i].genero = 'Arte'
        elif vector_libros[i].genero == 2:
            vector_libros[i].genero = 'Ficción'
        elif vector_libros[i].genero == 3:
            vector_libros[i].genero = 'Computación'
        elif vector_libros[i].genero == 4:
            vector_libros[i].genero = 'Economía'
        elif vector_libros[i].genero == 5:
            vector_libros[i].genero = 'Escolar'
        elif vector_libros[i].genero == 6:
            vector_libros[i].genero = 'Sociedad'
        elif vector_libros[i].genero == 7:
            vector_libros[i].genero = 'Gastronomía'
        elif vector_libros[i].genero == 8:
            vector_libros[i].genero = 'Infantil'
        elif vector_libros[i].genero == 9:
            vector_libros[i].genero = 'Otros'

        if vector_libros[i].idioma == 1:
            vector_libros[i].idioma = 'Español'
        elif vector_libros[i].idioma == 2:
            vector_libros[i].idioma = 'Inglés'
        elif vector_libros[i].idioma == 3:
            vector_libros[i].idioma = 'Francés'
        elif vector_libros[i].idioma == 4:
            vector_libros[i].idioma = 'Italiano'
        elif vector_libros[i].idioma == 5:
            vector_libros[i].idioma = 'Otro'

        print(chr(27) + '[1;107;40m' + '{:<27}'.format('Código ISBN: ' + vector_libros[i].codigo) + chr(27) + '[0m' +
              chr(27) + '[1;100;30m' + '{:<50}'.format(' -Título: ' + vector_libros[i].titulo) + chr(27) + '[0m' +
              chr(27) + '[1;107;40m' + '{:<25}'.format(' -Género: ' + vector_libros[i].genero) + chr(27) + '[0m' +
              chr(27) + '[1;100;30m' + '{:<20}'.format(' -Idioma: ' + vector_libros[i].idioma) + chr(27) + '[0m' +
              chr(27) + '[1;107;40m' + '{:<20}'.format(' -Costo: $' + str(vector_libros[i].costo) + chr(27) + '[0m'))


def carga_automatica(n):
    vec_libros = [None] * n
    for i in range(n):
        codigo = generar_isbn()
        titulo = generar_titulo()
        genero = random.randint(0, 9)
        idioma = random.randint(1, 5)
        precio = random.randint(100, 8000)
        vec_libros[i] = Libro(codigo, titulo, genero, idioma, precio)
    return vec_libros


def validar_codigo(code):
    codex = []
    for i in code:
        codex.append(i)
    ncode = []
    for i in code:
        if i != '-':
            ncode.append(i)

    ncode = ''.join(ncode)

    if len(ncode) == 10:
        ncodex = int(ncode[0]) * 10 + int(ncode[1]) * 9 + int(ncode[2]) * 8 + int(ncode[3]) * 7 + int(ncode[4]) * 6 + \
                    int(ncode[5]) * 5 + int(ncode[6]) * 4 + int(ncode[7]) * 3 + int(ncode[8]) * 2 + int(ncode[9])
    else:
        return False
    if ncodex % 11 == 0:
        num_ok = True
    else:
        num_ok = False

    cont = contx = 0
    pos_ant = 0
    pos_ok = code_ok = False
    for i in codex:
        code_ok = True
        cont += 1
        if i == '-':
            contx += 1
            pos_ant = cont
        if i == '-' and pos_ant == cont - 1:
            pos_ok = False
        if contx == 3 and len(codex) == 13 and pos_ok:
            code_ok = True
    if num_ok and code_ok:
        isbn_ok = True
    else:
        isbn_ok = False
    return isbn_ok


def carga_manual(n):
    vec_libros = [None] * n
    for k in range(n):
        codigo = input('\nIngrese el código ISBN del libro[' + str(k+1) + ']:')
        code_ok = False
        while not code_ok:
            code_ok = validar_codigo(codigo)
            if code_ok:
                print('Código ingresado correctamente')
            else:
                codigo = input('Ingrese un código ISBN válido: ')

        titulo = input('Ingrese el título del libro: ')
        print('(0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4: Economía,'
              ' 5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil, 9: Otros)')
        genero = int(input('Ingrese el número del género del libro: '))
        print('1) Español, 2) Inglés, 3) Francés, 4)Italiano, 5) Otros')
        idioma = int(input('Ingrese el número del idioma del libro: '))
        precio = int(input('Ingrese el precio del libro $: '))
        vec_libros[k] = Libro(codigo, titulo, genero, idioma, precio)
    return vec_libros


def ordenar_ascendente(vector_libros):
    for i in range(len(vector_libros)):
        for j in range(i+1, len(vector_libros)):
            if vector_libros[i].titulo > vector_libros[j].titulo:
                vector_libros[i].titulo, vector_libros[j].titulo = vector_libros[j].titulo, vector_libros[i].titulo
    return vector_libros


def ordenar_descentdente_costo(vector):
    for i in range(len(vector)):
        for j in range(i+1, len(vector)):
            if vector[i].costo < vector[j].costo:
                vector[i].costo, vector[j].costo = vector[j].costo, vector[i].costo
    return vector


def conteo_generos(vector_libros):
    vec_generos = [0] * 10
    for i in range(len(vector_libros)):
        if vector_libros[i].genero == 'Autoayuda':
            vec_generos[0] += 1
        elif vector_libros[i].genero == 'Arte':
            vec_generos[1] += 1
        elif vector_libros[i].genero == 'Ficción':
            vec_generos[2] += 1
        elif vector_libros[i].genero == 'Computación':
            vec_generos[3] += 1
        elif vector_libros[i].genero == 'Economía':
            vec_generos[4] += 1
        elif vector_libros[i].genero == 'Escolar':
            vec_generos[5] += 1
        elif vector_libros[i].genero == 'Sociedad':
            vec_generos[6] += 1
        elif vector_libros[i].genero == 'Gastronomía':
            vec_generos[7] += 1
        elif vector_libros[i].genero == 'Infantil':
            vec_generos[8] += 1
        elif vector_libros[i].genero == 'Otros':
            vec_generos[9] += 1

    in_may = vec_generos.index(max(vec_generos))

    if in_may == 0:
        may = 'Autoayuda'
    elif in_may == 1:
        may = 'Arte'
    elif in_may == 2:
        may = 'Ficción'
    elif in_may == 3:
        may = 'Computación'
    elif in_may == 4:
        may = 'Economía'
    elif in_may == 5:
        may = 'Escolar'
    elif in_may == 6:
        may = 'Sociedad'
    elif in_may == 7:
        may = 'Gastronomía'
    elif in_may == 8:
        may = 'Infantil'
    elif in_may == 9:
        may = 'Otros'

    return vec_generos, may


def listar_libros_genero(vector_libros, gen_may):
    vector_precios = []
    for i in range(len(vector_libros)):
        if vector_libros[i].genero == gen_may:
            vector_precios.append(vector_libros[i])
            ordenar_descentdente_costo(vector_precios)
    return vector_precios


def mostrar_datos_vector(vector_libros, idx):
    print('Código ISBN:', vector_libros[idx].codigo, end=' - ')
    print('Título:', vector_libros[idx].titulo, end=' - ')
    print('Género:', vector_libros[idx].genero, end=' - ')
    print('Idioma:', vector_libros[idx].idioma, end=' - ')
    print('Precio:$', vector_libros[idx].costo)


def write(libro):
    print('Código:', str(libro.codigo), ' - ', 'Título:', str(libro.titulo), ' - ', 'Género:', str(libro.genero),
          ' - ', 'Idioma:', str(libro.idioma), ' - ', 'Costo:$', str(libro.costo))


def busqueda_idiomas(vector_libros, x):
    idi = ''
    if x == 1:
        idi = 'Español'
    elif x == 2:
        idi = 'Inglés'
    elif x == 3:
        idi = 'Francés'
    elif x == 4:
        idi = 'Italiano'
    elif x == 5:
        idi = 'Otros'

    idx = -1
    may = 0
    no_hay = True
    for i in range(len(vector_libros)):
        if vector_libros[i].idioma == idi:
            no_hay = False
            if int(vector_libros[i].costo) > may:
                may = vector_libros[i].costo
                idx = i
    if no_hay:
        return 'No hay libros en ese idioma.'
    else:
        print('El libro más caro es:')
        return mostrar_datos_vector(vector_libros, idx)


def busqueda_isbn(vector_libros, isbn):
    saw = False
    for i in range(len(vector_libros)):
        if vector_libros[i].codigo == isbn:
            saw = True
            vector_libros[i].costo = vector_libros[i].costo + vector_libros[i].costo * 0.10
            print('El libro que posee ese isbn es:')
            write(vector_libros[i])
    if not saw:
        print('No hay libro con ese isbn')


def consulta_por_grupo(vector_libros, vec_isbns):
    disponibles = []
    for i in range(len(vector_libros)):
        if vector_libros[i].codigo in vec_isbns:
            disponibles.append(vector_libros[i])
    return disponibles

def filtrar_matriz(vector, filas, columnas):
    mat = [[None] * columnas for i in range(filas)]

    for elemento in vector:
        col = elemento.tema1
        fil = elemento.tema2


