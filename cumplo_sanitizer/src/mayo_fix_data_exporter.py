import csv

# The source of the fix_data.csv for mayo profile is this: 

fix_data = [
    ['27555', 'avanza construccion ltda', '2016-Sep-05', (513363 - 477954), 0], # ==> (cumplo earnings) 513363 - (calculated earnings) 477954
    ['27761', 'Comercial 2050', '2016-Nov-11', (512505 - 502636), 0],
    ['28106', 'avendaño y aranda', '2016-May-05', (552636), 0], #  ==> late payment with garantee
    ['28948', 'ingecom', '2016-Dec-20', (523218 - 266189), 0],
    ['29515', 'abratec', '2017-May-17', (526314 - 268030), 0],
    ['29597', 'hurtado bombeo de hormigon', '2016-12-22', (503075), 0], # >> not executed & 'not returned' on records
    ['29602', 'IC FENIX', '2017-04-12', (519536-393921), 0],
    ['29933', 'teur chile spa', '2017-06-30', (523371-397112), 0],
    ['30065', 'dolphins', '2017-05-16', (517679*2 - 522411), 0], # doble investment
    ['30494', 'hincavial', '2017-05-08', (513705 - 304807), 0],
    ['30495', 'milla tires', '2017-06-29', (208986 - 158064), 0],
    ['30809', 'hincavial', '2017-05-25', (1017105 - 977689), 0],
    ['30968', 'universidad del pacifico', '2017-08-29', (518219 - 506606), 0],
    ['31045', 'Reminisen', '2017-07-04', (507658 - 474709), 0],
    ['31047', 'Reminisen', '2017-08-14', (515142 - 486962), 0],
    ['31193', 'transportes roll', '2017-06-10', (516323 - 262341), 0],
    ['31220', 'MONTAJES M&S', '2017-06-1', (508177- 1125), 0],
    ['31288', 'Alimil', '2017-05-24', (507692 - 51025), 0],
    ['31406', 'pl trading', '2017-10-30', (527679 - 445604), 0],
    ['31426', 'Uno Market', '2017-09-11', (310583 - 235711), 0],
    ['31453', 'Uno Market', '2017-06-13', (505205 - 56956), 0],
    ['31465', 'policart curico', '2017-12-06', (539046 - 407112), 0],
    ['31516', 'servicur', '2017-06-05', (503906 - 51232), 0],
    ['31521', 'proyecto propio', '2017-06-13', (1009864 - 753078), 0],
    ['31950', 'ragori', '2017-10-19', (1037186 - 795855), 0],
    ['32146', 'constructora jose y jose', '2017-06-19', (1020664 - 3800), 0],
    ['32224', 'constructora jose y jose', '2017-09-06', (509450 - 1925), 0],
    ['32226', 'viveros chile', '2017-10-05', (517179 - 2350), 0],
    ['32326', 'reminisen', '2017-08-31', (2036499 - 1914828), 0],
    ['32327', 'reminisen', '2017-09-01', (511265 - 338937), 0],
    ['32438', 'universidad del pacifico', '2017-09-01', (309147 - 86562), 0],
    ['32466', 'ingecom', '2017-10-26', (522465 - 3050), 0],
    ['32548', 'comercial 2050', '2017-11-29', (519553 - 186042), 0],
    ['32730', 'reminisen', '2017-11-16', (508410 - 352355), 0],
    ['32846', 'constructora arbeit', '2017-09-21', (202296 - 259), 0],
    ['32885', 'reminisen', '2017-10-30', (204399 - 730), 0],
    ['33060', 'dyma radios', '2018-01-19', (519592 - 420829), 0],
    ['33181', 'ingecom', '2017-09-13', (1015163 - 4450), 0],
    ['33217', 'r y r ltda', '2017-10-19', (508358 - 1275), 0],
    ['33661', 'social it', '2017-09-26', (503095 - 1237), 0],
    ['33675', 'murano ltda', '2017-09-27', (505761 - 700), 0],
    ['33728', 'dolphins', '2017-11-14', (509900 - 2200), 0],
    ['33743', 'hincavial', '2017-10-26', (504501 - 1237), 0],
    ['33763', 'comercial 2050', '2018-01-09', (509474 - 249462), 0],
    ['33765', 'viveros chile', '2018-06-25', ((504000 + 404000 ) - 408132), 0], #>> super weird, $500k not returned?)
    ['33819', 'sdi', '2017-12-08', (304781 - 242884), 0],
    ['34371', 'tres ingenieria', '2018-02-22', (520777 - 351904), 0],
    ['64085', 'orion spa', '2022-11-30', (626857 - 474383), 0],
    ['64210', 'disenar ltda', '2022-11-24', (1024384 - 0), 0],
    ['64307', 'aquasys 2', '2022-09-21', (1113424 - 0), 0],
    ['64924', 'constructora calafate spa', '2022-12-01', (1028664 - 0), 0],
    ['65196', 'constructora rsm spa', '2022-11-24', (1024646 - 0), 0],
    ['65199', 'cotar', '2022-11-17', (1016787 - 0), 0],
    ['65207', 'disenar ltda', '2022-12-27', (1038743 - 0), 0],
    ['65222', 'constructora felipe hernan', '2022-12-01', (511049 - 0), 0],
    ['65258', 'JOSE MIGUEL CARREÑO FIGUEROA', '2022-12-02', (1025760 - 529851), 0],
    ['65668', 'Las Cumbres', '2023-01-24', (517500 - 0), 0],
    ['65939', 'CONSTRUCTORA PAZ E.I.R.L', '2022-12-06', (1015668 - 0 ), 0],
    ['66009', 'VICTOR ALMONACID', '2023-02-09', (102952 - 0), 0],
    ['66010', 'vibrados y construcciones carlos novoa espinoza eirl', '2023-01-25', (514500 * 2 - 0), 0],
    ['66019', 'Comercial 2050', '2023-01-19', (506558 * 2 - 689021), 0],

    ['72775', 'QUINTA SOLAR LIMITADA', '2023-09-29', 1166, 0],

    # ['----------' real late >>  32104, constructora scc, 2020-12-02, - 496612.0],
    # ['----------' real late >> 42148, ce gourmet, 2019-08-01, 450.950 - 452363.0],
    # ['----------' real late >> 48759, chile moda, 2021-12-29, - 481602.0],
    # ['----------' real late >> 48925, ogm equipos y maquinarias sa, 2023-06-12, - 232413.0],
    # ['----------' real late >> 49119, chile moda, 2021-12-29, - 261141.0],
    # ['----------' real late >> 49853, peuma, 2019-10-21, - 1410.0],
    # ['----------' real late >> 49948, o.g.m. obras y montajes s.a, 2023-09-26, - 189635.0],
    # ['----------' real late >> 50403, peuma, 2019-12-06, - 1840.0],
    # ['----------' real late >> 50563, o.g.m. obras y montajes s.a, 2023-09-26, - 76659.0],
    # ['----------' real late >> 50683, peuma, 2019-12-02, - 1365.0],
    # ['----------' real late >> 62698, mf sistemas, 2022-07-09, - 130918.0],
]

# Nombre del archivo CSV de salida
csv_filename = './data_in/fix_data.csv'

# Abre el archivo CSV en modo escritura
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Escribe el encabezado
    csv_writer.writerow(['ID', 'Nombre', 'Fecha', 'Valor', 'Campo'])

    # Escribe los datos de la lista en el archivo CSV
    for item in fix_data:
        csv_writer.writerow(item)

# Test-Print !
data = []
with open(csv_filename, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Lee el encabezado (si existe)
    header = next(csv_reader, None)
   
    # Lee las filas de datos
    for row in csv_reader:
        data.append(row)

for row in data:
    print(row)
    print(row)
