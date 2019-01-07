import psycopg2
from model.Rol import Rol
from model.Producto import Producto
from model.CategoriaProducto import CategoriaProducto
from model.Sucursal import Sucursal
from model.Usuario import Usuario

class Manager:

    def __init__(self):
        self.PSQL_HOST = "localhost"
        self.PSQL_PORT = "5432"
        self.PSQL_USER = "postgres"
        self.PSQL_PASS = "postgres"
        self.PSQL_DB = "ControlSystem"
    
    def crearConexion(self):
        stringConexion = "host=%s port=%s user=%s password=%s dbname=%s" % (self.PSQL_HOST, self.PSQL_PORT, self.PSQL_USER, self.PSQL_PASS, self.PSQL_DB)
        self.conn = psycopg2.connect(stringConexion)
    
    def iniciar(self):
        self.crearConexion()
    
    def listarRoles(self):
        query = "SELECT  * FROM roles"
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        roles = []
        for row in rows:
            roles.append(Rol(row[0], row[1], row[2]))
        cur.close()            
        return roles

    def listarCategoriasProducto(self):
        query = "SELECT * FROM categoria_producto"    
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        categorias = []
        for row in rows:
            categorias.append(CategoriaProducto(row[0], row[1]))
        cur.close()            
        return categorias

    def listarProductos(self):
        query = "SELECT * FROM producto"
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        productos = []
        for row in rows:
            productos.append(Producto(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        cur.close()
        return productos
    
    def crearProducto(self, producto):
        query = "INSERT INTO producto (descripcion, id_categoria, precio, stock_minimo, stock_actual, id_sucursal) VALUES (%s, %s, %s, %s, %s, %s)"
        queryOk = query, (producto.descripcion, producto.idCategoria, producto.precio, producto.stockMinimo, producto.stockActual, producto.idSucursal)
        cur = self.conn.cursor()
        cur.execute(query, (producto.descripcion, producto.idCategoria, producto.precio, producto.stockMinimo, producto.stockActual, producto.idSucursal))
        self.conn.commit()
        cur.close()
        return True

    def buscarCategoriaPorId(self, idCategoria):
        query = "SELECT * FROM categoria_producto WHERE id_categoria = " + str(idCategoria)
        cur = self.conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        categoria = CategoriaProducto(row[0], row[1])
        cur.close()
        return categoria
    
    def buscarSucursalPorId(self, idSucursal):
        query = "SELECT * FROM sucursal_negocio WHERE id_sucursal = " + str(idSucursal)
        cur = self.conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        sucursal = Sucursal(row[0], row[1], row[2], row[3], row[4])
        cur.close()
        return sucursal
    
    def iniciarSesion(self, username, password):
        return self.validarCredenciales(username, password)
    
    def validarCredenciales(self, username, password):
        query = "SELECT * FROM usuario WHERE username = '" + username + "' AND password = '" + password + "'"
        cur = self.conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        usuario = None
        if row is not None:
            usuario = Usuario(row[0], row[3], row[1], row[2], row[4])
        return usuario
    
    def buscarSucursalesDeUsuario(self, idUsuario):
        query = "SELECT * FROM sucursal_negocio sn JOIN usuarios_sucursal us ON us.id_usuario = \
                " + str(idUsuario) + " AND us.id_sucursal = sn.id_sucursal"
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        sucursales = []
        for row in rows:
            sucursales.append(Sucursal(row[0], row[1], row[2], row[3], row[4]))
        cur.close()
        return sucursales
