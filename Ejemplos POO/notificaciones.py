import time
from functools import wraps

# Ejemplo de IA. Revisar

# ==================== DECORADOR ====================
def log_notificaciones(func):
    """Decorador que registra el tiempo y contenido de cada notificación"""

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"\n[LOG] Enviando notificación a las {time.strftime('%H:%M:%S')}")
        print(f"[LOG] Método: {func.__name__}")
        resultado = func(self, *args, **kwargs)
        print(f"[LOG] Destinatario: {self.destinatario}")
        print(f"[LOG] Estado: {'✅ Enviado' if resultado else '❌ Falló'}")
        return resultado

    return wrapper


# ==================== CLASES BASE ====================
class Email:
    """Clase base para envío de emails"""

    def __init__(self, destinatario, asunto):
        self.destinatario = destinatario
        self.asunto = asunto

    @log_notificaciones
    def enviar(self, mensaje):
        print(f"📧 Enviando email a {self.destinatario}")
        print(f"   Asunto: {self.asunto}")
        print(f"   Mensaje: {mensaje}")
        return True


class SMS:
    """Clase base para envío de SMS"""

    def __init__(self, destinatario, telefono):
        self.destinatario = destinatario
        self.telefono = telefono

    @log_notificaciones
    def enviar(self, mensaje):
        # Limitar mensaje a 160 caracteres (como SMS real)
        if len(mensaje) > 160:
            print(f"⚠️  SMS truncado a 160 caracteres")
            mensaje = mensaje[:157] + "..."

        print(f"📱 Enviando SMS al {self.telefono}")
        print(f"   Mensaje: {mensaje}")
        return True


# ==================== HERENCIA MÚLTIPLE ====================
class NotificacionWhatsApp(Email, SMS):
    """Simula notificaciones por WhatsApp combinando email y SMS"""

    def __init__(self, destinatario, telefono, nombre):
        # Llamamos a los constructores de ambas clases base
        Email.__init__(self, destinatario, f"WhatsApp para {nombre}")
        SMS.__init__(self, destinatario, telefono)
        self.nombre = nombre
        self.archivos_adjuntos = []

    def adjuntar_archivo(self, archivo):
        """Método específico de WhatsApp"""
        self.archivos_adjuntos.append(archivo)
        print(f"📎 Archivo adjuntado: {archivo}")

    # Sobrescribimos el método enviar para combinar funcionalidades
    @log_notificaciones
    def enviar(self, mensaje):
        # Usamos la funcionalidad de SMS para el texto
        print(f"💬 Enviando WhatsApp a {self.nombre} ({self.telefono})")

        # Mostramos los archivos adjuntos si los hay
        if self.archivos_adjuntos:
            print(f"   📎 Adjuntos: {', '.join(self.archivos_adjuntos)}")

        # Reutilizamos el método de SMS para enviar el mensaje
        resultado_sms = super().enviar(mensaje)

        # Si hay email configurado, enviamos también por email (copia)
        if hasattr(self, 'asunto') and self.asunto:
            print(f"   📧 Enviando copia por email a {self.destinatario}")
            Email.enviar(self, mensaje)

        return resultado_sms

    # ==================== MÉTODOS MÁGICOS ====================
    def __str__(self):
        """Representación amigable para usuarios"""
        return f"WhatsApp de {self.nombre} (📱{self.telefono} | 📧{self.destinatario})"

    def __repr__(self):
        """Representación técnica para depuración"""
        return f"NotificacionWhatsApp('{self.destinatario}', '{self.telefono}', '{self.nombre}')"

    def __len__(self):
        """Retorna cantidad de archivos adjuntos"""
        return len(self.archivos_adjuntos)

    def __eq__(self, other):
        """Compara si son el mismo contacto"""
        if isinstance(other, NotificacionWhatsApp):
            return (self.telefono == other.telefono and
                    self.destinatario == other.destinatario)
        return False

    def __call__(self, mensaje):
        """Permite llamar al objeto como si fuera una función"""
        return self.enviar(mensaje)


# ==================== DEMOSTRACIÓN PRÁCTICA ====================
if __name__ == "__main__":
    print("=" * 50)
    print("SISTEMA DE NOTIFICACIONES MULTI-CANAL")
    print("=" * 50)

    # Crear una notificación de WhatsApp
    whatsapp1 = NotificacionWhatsApp(
        destinatario="cliente@empresa.com",
        telefono="+34 600 123 456",
        nombre="María García"
    )

    # Demostración de __str__ y __repr__
    print("\n📋 Información del contacto:")
    print(str(whatsapp1))  # __str__
    print(repr(whatsapp1))  # __repr__

    # Adjuntar archivos y ver longitud
    whatsapp1.adjuntar_archivo("factura.pdf")
    whatsapp1.adjuntar_archivo("manual.pdf")
    print(f"\n📎 Archivos adjuntos: {len(whatsapp1)}")  # __len__

    # Enviar notificación
    print("\n📤 Enviando notificación:")
    whatsapp1("¡Hola María! Tu pedido ha sido enviado. 😊")

    # Comparar contactos
    whatsapp2 = NotificacionWhatsApp(
        destinatario="cliente@empresa.com",
        telefono="+34 600 123 456",
        nombre="María García"
    )

    whatsapp3 = NotificacionWhatsApp(
        destinatario="otro@cliente.com",
        telefono="+34 600 789 012",
        nombre="Carlos López"
    )

    print("\n🔍 Comparando contactos:")
    print(f"¿Son el mismo contacto? {whatsapp1 == whatsapp2}")  # __eq__
    print(f"¿Son el mismo contacto? {whatsapp1 == whatsapp3}")

    # Uso como función (__call__)
    print("\n🎯 Usando el objeto como función:")
    whatsapp1("Mensaje enviado usando __call__")