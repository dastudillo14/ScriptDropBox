import dropbox

dbx = dropbox.Dropbox('su_token')
#token obtenido en dropbox developers
ruta_Dbx = '/Mis_Datos/'
#ruta para guardar en una carpeta especifica dentro de DropBox sus archivos

name_file= 'ejemplo.txt'
archivo = open(name_file,'rb')

dbx.files_upload(archivo.read() ,ruta_Dbx + name_file)

print("Archivo "+name_file+" fue subido con èxito")


