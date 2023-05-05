import mis_registros as mr


def main():
    print('{:^40}'.format(chr(27) + "[4;35m" + '-->GESTIÓN DE LIBROS' + chr(27) + "[0m"))
    carga_ok = carga3 = False
    mr.menu()
    op = int(input('Ingrese el número de menú: '))
    while op != 0:
        if op == 1:
            n = int(input('Ingrese la cantidad de libros a cargar: '))
            vec_libros = mr.carga_manual(n)
            mr.ordenar_ascendente(vec_libros)
            mr.mostrar_todo(vec_libros)
            carga_ok = True
            mr.menu()
            op = int(input('Ingrese el número de menú: '))

        elif op == 2:
            n = int(input('Ingrese la cantidad de libros a cargar: '))
            vec_libros = mr.carga_automatica(n)
            mr.ordenar_ascendente(vec_libros)
            mr.mostrar_todo(vec_libros)
            carga_ok = True
            input()
            mr.menu()
            op = int(input('Ingrese el número de menú: '))

        elif op == 3:
            if carga_ok:

                vec_generos, may = mr.conteo_generos(vec_libros)
                print('\n')
                print(chr(27) + "[3;32m" + '---Cantidad de libros según género---' + chr(27) + "[0m")
                print('{:^35}'.format('Autoayuda: ' + str(vec_generos[0])))
                print('{:^35}'.format('Arte: ' + str(vec_generos[1])))
                print('{:^35}'.format('Ficción: ' + str(vec_generos[2])))
                print('{:^35}'.format('Computación: ' + str(vec_generos[3])))
                print('{:^35}'.format('Econimía: ' + str(vec_generos[4])))
                print('{:^35}'.format('Escolar: ' + str(vec_generos[5])))
                print('{:^35}'.format('Sociedad: ' + str(vec_generos[6])))
                print('{:^35}'.format('Gastronomía: ' + str(vec_generos[7])))
                print('{:^35}'.format('Infantil: ' + str(vec_generos[8])))
                print('{:^35}'.format('Otros: ' + str(vec_generos[9])))
                print(chr(27) + "[3;32m" + 'El género con más libros es ' + may + chr(27) + "[0m")
                carga3 = True
            else:
                print('Primero debe ingresar libros.')
                input()
            input()
            mr.menu()
            op = int(input('Ingrese el número de menú: '))

        elif op == 4:
            if carga_ok:
                print('1: español, 2: inglés, 3: francés, 4:italiano, 5:otros')
                idi = int(input('Ingrese el número de idioma: '))
                el_may = mr.busqueda_idiomas(vec_libros, idi)
                print(el_may)
            else:
                print('Primero debe ingresar libros.')
                input()
            input()
            mr.menu()
            op = int(input('Ingrese el número de menú: '))

        elif op == 5:
            if carga_ok:
                isbn = input('Ingrese el ISBN del libro: ')
                code_ok = False
                while not code_ok:
                    code_ok = mr.validar_codigo(isbn)
                    if code_ok:
                        print('Código ingresado correctamente')
                        mr.busqueda_isbn(vec_libros, isbn)
                    else:
                        isbn = input('Ingrese un código ISBN válido: ')
            else:
                print('Primero debe ingresar libros.')
            input()
            mr.menu()
            op = int(input('Ingrese el número de menú: '))

        elif op == 6:
            if carga_ok and carga3:
                vec_precios = mr.listar_libros_genero(vec_libros, may)
                for i in range(len(vec_precios)):
                    mr.write(vec_precios[i])
            else:
                print('Primero debe ingresar libros e ingresar la opción 3.')
                input()
            input()
            print('\n')
            mr.menu()
            op = int(input('Ingrese el número de menú: '))

        elif op == 7:
            if carga_ok:
                vec_isbns = []
                n = int(input('Ingrese el número de libros a buscar: '))
                for i in range(n):
                    isbn = input('Ingrese el ISBN del libro: ')
                    code_ok = False
                    while not code_ok:
                        code_ok = mr.validar_codigo(isbn)
                        if code_ok:
                            print(chr(27) + '[1;32m' + 'Código ingresado correctamente' + chr(27) + '[0m')
                            vec_isbns.append(isbn)
                        else:
                            isbn = input('Ingrese un código ISBN válido: ')
                dispo = mr.consulta_por_grupo(vec_libros, vec_isbns)
                print('\nLibros disponibles:')
                mr.mostrar_todo(dispo)

            else:
                print('Primero deben ingresar libros.')
                input()
            mr.menu()
            op = int(input('Ingrese el número de menú:'))

        else:
            print('Ingrese un número de menú correcto.')
            input()
            mr.menu()
            op = int(input('Ingrese el número de menú: '))


if __name__ == '__main__':
    main()
