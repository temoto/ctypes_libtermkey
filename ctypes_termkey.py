from ctypes import *

_libraries = {}
_libraries['libtermkey.so.0'] = CDLL('libtermkey.so.0')
STRING = c_char_p

# values for enumeration 'termkey_sym'
TERMKEY_SYM_UNKNOWN = -1
TERMKEY_SYM_NONE = 0
TERMKEY_SYM_BACKSPACE = 1
TERMKEY_SYM_TAB = 2
TERMKEY_SYM_ENTER = 3
TERMKEY_SYM_ESCAPE = 4
TERMKEY_SYM_SPACE = 5
TERMKEY_SYM_DEL = 6
TERMKEY_SYM_UP = 7
TERMKEY_SYM_DOWN = 8
TERMKEY_SYM_LEFT = 9
TERMKEY_SYM_RIGHT = 10
TERMKEY_SYM_BEGIN = 11
TERMKEY_SYM_FIND = 12
TERMKEY_SYM_INSERT = 13
TERMKEY_SYM_DELETE = 14
TERMKEY_SYM_SELECT = 15
TERMKEY_SYM_PAGEUP = 16
TERMKEY_SYM_PAGEDOWN = 17
TERMKEY_SYM_HOME = 18
TERMKEY_SYM_END = 19
TERMKEY_SYM_CANCEL = 20
TERMKEY_SYM_CLEAR = 21
TERMKEY_SYM_CLOSE = 22
TERMKEY_SYM_COMMAND = 23
TERMKEY_SYM_COPY = 24
TERMKEY_SYM_EXIT = 25
TERMKEY_SYM_HELP = 26
TERMKEY_SYM_MARK = 27
TERMKEY_SYM_MESSAGE = 28
TERMKEY_SYM_MOVE = 29
TERMKEY_SYM_OPEN = 30
TERMKEY_SYM_OPTIONS = 31
TERMKEY_SYM_PRINT = 32
TERMKEY_SYM_REDO = 33
TERMKEY_SYM_REFERENCE = 34
TERMKEY_SYM_REFRESH = 35
TERMKEY_SYM_REPLACE = 36
TERMKEY_SYM_RESTART = 37
TERMKEY_SYM_RESUME = 38
TERMKEY_SYM_SAVE = 39
TERMKEY_SYM_SUSPEND = 40
TERMKEY_SYM_UNDO = 41
TERMKEY_SYM_KP0 = 42
TERMKEY_SYM_KP1 = 43
TERMKEY_SYM_KP2 = 44
TERMKEY_SYM_KP3 = 45
TERMKEY_SYM_KP4 = 46
TERMKEY_SYM_KP5 = 47
TERMKEY_SYM_KP6 = 48
TERMKEY_SYM_KP7 = 49
TERMKEY_SYM_KP8 = 50
TERMKEY_SYM_KP9 = 51
TERMKEY_SYM_KPENTER = 52
TERMKEY_SYM_KPPLUS = 53
TERMKEY_SYM_KPMINUS = 54
TERMKEY_SYM_KPMULT = 55
TERMKEY_SYM_KPDIV = 56
TERMKEY_SYM_KPCOMMA = 57
TERMKEY_SYM_KPPERIOD = 58
TERMKEY_SYM_KPEQUALS = 59
termkey_sym = c_int # enum

# values for enumeration 'termkey_type'
TERMKEY_TYPE_UNICODE = 0
TERMKEY_TYPE_FUNCTION = 1
TERMKEY_TYPE_KEYSYM = 2
termkey_type = c_int # enum

# values for enumeration 'termkey_result'
TERMKEY_RES_NONE = 0
TERMKEY_RES_KEY = 1
TERMKEY_RES_EOF = 2
TERMKEY_RES_AGAIN = 3
termkey_result = c_int # enum
termkey_keysym = c_int
class termkey(Structure):
    pass
termkey_t = termkey
termkey_check_version = _libraries['libtermkey.so.0'].termkey_check_version
termkey_check_version.restype = None
termkey_check_version.argtypes = [c_int, c_int]
termkey_new = _libraries['libtermkey.so.0'].termkey_new
termkey_new.restype = POINTER(termkey_t)
termkey_new.argtypes = [c_int, c_int]
termkey_free = _libraries['libtermkey.so.0'].termkey_free
termkey_free.restype = None
termkey_free.argtypes = [POINTER(termkey_t)]
termkey_destroy = _libraries['libtermkey.so.0'].termkey_destroy
termkey_destroy.restype = None
termkey_destroy.argtypes = [POINTER(termkey_t)]
termkey_get_flags = _libraries['libtermkey.so.0'].termkey_get_flags
termkey_get_flags.restype = c_int
termkey_get_flags.argtypes = [POINTER(termkey_t)]
termkey_set_flags = _libraries['libtermkey.so.0'].termkey_set_flags
termkey_set_flags.restype = None
termkey_set_flags.argtypes = [POINTER(termkey_t), c_int]
termkey_set_waittime = _libraries['libtermkey.so.0'].termkey_set_waittime
termkey_set_waittime.restype = None
termkey_set_waittime.argtypes = [POINTER(termkey_t), c_int]
termkey_get_waittime = _libraries['libtermkey.so.0'].termkey_get_waittime
termkey_get_waittime.restype = c_int
termkey_get_waittime.argtypes = [POINTER(termkey_t)]
class termkey_key(Structure):
    pass
termkey_getkey = _libraries['libtermkey.so.0'].termkey_getkey
termkey_getkey.restype = termkey_result
termkey_getkey.argtypes = [POINTER(termkey_t), POINTER(termkey_key)]
termkey_getkey_force = _libraries['libtermkey.so.0'].termkey_getkey_force
termkey_getkey_force.restype = termkey_result
termkey_getkey_force.argtypes = [POINTER(termkey_t), POINTER(termkey_key)]
termkey_waitkey = _libraries['libtermkey.so.0'].termkey_waitkey
termkey_waitkey.restype = termkey_result
termkey_waitkey.argtypes = [POINTER(termkey_t), POINTER(termkey_key)]
size_t = c_ulong
termkey_pushinput = _libraries['libtermkey.so.0'].termkey_pushinput
termkey_pushinput.restype = None
termkey_pushinput.argtypes = [POINTER(termkey_t), POINTER(c_ubyte), size_t]
termkey_advisereadable = _libraries['libtermkey.so.0'].termkey_advisereadable
termkey_advisereadable.restype = termkey_result
termkey_advisereadable.argtypes = [POINTER(termkey_t)]
termkey_register_keyname = _libraries['libtermkey.so.0'].termkey_register_keyname
termkey_register_keyname.restype = termkey_keysym
termkey_register_keyname.argtypes = [POINTER(termkey_t), termkey_keysym, STRING]
termkey_get_keyname = _libraries['libtermkey.so.0'].termkey_get_keyname
termkey_get_keyname.restype = STRING
termkey_get_keyname.argtypes = [POINTER(termkey_t), termkey_keysym]

# values for enumeration 'termkey_format'
TERMKEY_FORMAT_LONGMOD = 1
TERMKEY_FORMAT_CARETCTRL = 2
TERMKEY_FORMAT_ALTISMETA = 4
TERMKEY_FORMAT_WRAPBRACKET = 8
termkey_format = c_int # enum
termkey_snprint_key = _libraries['libtermkey.so.0'].termkey_snprint_key
termkey_snprint_key.restype = size_t
termkey_snprint_key.argtypes = [POINTER(termkey_t), STRING, size_t, POINTER(termkey_key), termkey_format]
termkey_key._fields_ = [
        ('type_', termkey_type),
        ('code', c_ulong),
        ('modifiers', c_int),
        ('utf8', c_char * 7),
]
termkey._fields_ = [
]


# shortcuts over ctypes code generation
class Result(object):
    NONE = 0
    KEY = 1
    EOF = 2
    AGAIN = 3


class KeyType(object):
    UNICODE = 0
    FUNCTION = 1
    KEYSYM = 2


class KeyModifier(object):
    SHIFT = 1 << 0
    ALT   = 1 << 1
    CTRL  = 1 << 2


def check_termkey_pointer(func):
    def wrapped(self, *args, **kwargs):
        if not self._tk:
            raise Exception("TermKey is not initialized. Create another TermKey object.")
        return func(self, *args, **kwargs)
    return wrapped


class TermKey(object):
    def __init__(self, fd=0, flags=0):
        self.sprint_buffer_size = 50
        self._tk = termkey_new(fd, flags)

    def __del__(self):
        self.close()

    def close(self):
        if self._tk:
            termkey_destroy(self._tk)
            self._tk = None

    @check_termkey_pointer
    def set_waittime(self, time):
        termkey_set_waittime(self._tk, time)

    @check_termkey_pointer
    def get_waittime(self):
        return termkey_get_waittime(self._tk)

    @check_termkey_pointer
    def get_flags(self):
        return termkey_get_flags(self._tk)

    @check_termkey_pointer
    def set_flags(self, new_flags):
        termkey_set_flags(self, new_flags)

    @check_termkey_pointer
    def getkey(self):
        new_key = termkey_key()
        result = termkey_getkey(self._tk, new_key)
        return result, new_key

    @check_termkey_pointer
    def getkey_force(self):
        new_key = termkey_key()
        result = termkey_getkey_force(self._tk, new_key)
        return result, new_key

    @check_termkey_pointer
    def waitkey(self):
        new_key = termkey_key()
        result = termkey_waitkey(self._tk, new_key)
        return result, new_key

    @check_termkey_pointer
    def pushinput(self, input_):
        inputlen = len(input_)
        termkey_pushinput(self._tk, input_, inputlen)

    @check_termkey_pointer
    def advisereadable(self):
        return termkey_advisereadable(self._tk)

    @check_termkey_pointer
    def termkey_register_keyname(self, sym, name):
        return termkey_register_keyname(self._tk, sym, name)

    @check_termkey_pointer
    def termkey_get_keyname(self, sym):
        return termkey_get_keyname(self._tk, sym)

    @check_termkey_pointer
    def sprint_key(self, key, format=0):
        buf = '\0' * self.sprint_buffer_size
        real_size = termkey_snprint_key(self._tk, buf, len(buf), key, format)
        if real_size < self.sprint_buffer_size:
            buf = buf[:real_size]
            return buf
        else:
            raise Exception("Key sprint value doesn't fit %d bytes"
                    % (self.sprint_buffer_size,))


__all__ = ['TERMKEY_SYM_REFRESH', 'TERMKEY_SYM_PAGEUP',
           'TERMKEY_SYM_PAGEDOWN', 'size_t', 'TERMKEY_SYM_DELETE',
           'termkey_register_keyname', 'termkey_set_flags',
           'TERMKEY_SYM_RESUME', 'TERMKEY_SYM_REDO',
           'TERMKEY_SYM_COPY', 'TERMKEY_SYM_SUSPEND',
           'TERMKEY_SYM_COMMAND', 'TERMKEY_RES_KEY',
           'TERMKEY_FORMAT_LONGMOD', 'TERMKEY_SYM_UNDO',
           'TERMKEY_SYM_HELP', 'termkey_keysym',
           'TERMKEY_TYPE_KEYSYM', 'TERMKEY_RES_NONE',
           'termkey_get_flags', 'TERMKEY_SYM_UP', 'TERMKEY_SYM_DOWN',
           'TERMKEY_SYM_OPTIONS', 'TERMKEY_SYM_BEGIN',
           'TERMKEY_SYM_NONE', 'termkey_set_waittime',
           'termkey_destroy', 'termkey_waitkey',
           'termkey_advisereadable', 'TERMKEY_TYPE_FUNCTION',
           'TERMKEY_RES_AGAIN', 'TERMKEY_SYM_RIGHT',
           'termkey_pushinput', 'termkey_check_version',
           'TERMKEY_SYM_KP9', 'TERMKEY_SYM_REFERENCE', 'termkey_key',
           'TERMKEY_SYM_REPLACE', 'TERMKEY_SYM_ESCAPE', 'termkey_sym',
           'TERMKEY_FORMAT_ALTISMETA', 'TERMKEY_SYM_MARK',
           'termkey_format', 'TERMKEY_RES_EOF', 'TERMKEY_SYM_LEFT',
           'TERMKEY_SYM_CLEAR', 'TERMKEY_SYM_INSERT',
           'TERMKEY_SYM_KPEQUALS', 'TERMKEY_SYM_KPENTER',
           'termkey_getkey_force', 'TERMKEY_SYM_KPMULT',
           'TERMKEY_SYM_KPPERIOD', 'TERMKEY_SYM_KPPLUS',
           'TERMKEY_FORMAT_CARETCTRL', 'termkey_new',
           'TERMKEY_SYM_MESSAGE', 'termkey_get_waittime',
           'TERMKEY_SYM_OPEN', 'TERMKEY_SYM_MOVE', 'termkey_getkey',
           'TERMKEY_SYM_KP8', 'termkey_result', 'TERMKEY_SYM_KP6',
           'TERMKEY_SYM_KP7', 'TERMKEY_SYM_KP4', 'TERMKEY_SYM_KP5',
           'TERMKEY_SYM_KP2', 'TERMKEY_SYM_KP3', 'TERMKEY_SYM_KP0',
           'TERMKEY_SYM_KP1', 'TERMKEY_SYM_RESTART',
           'TERMKEY_SYM_CANCEL', 'termkey_type',
           'termkey_snprint_key', 'termkey_free',
           'TERMKEY_SYM_KPMINUS', 'termkey_t', 'TERMKEY_SYM_SAVE',
           'TERMKEY_SYM_END', 'TERMKEY_SYM_SPACE',
           'TERMKEY_SYM_PRINT', 'TERMKEY_SYM_HOME',
           'TERMKEY_SYM_KPDIV', 'termkey_get_keyname',
           'TERMKEY_SYM_BACKSPACE', 'TERMKEY_FORMAT_WRAPBRACKET',
           'TERMKEY_SYM_UNKNOWN', 'TERMKEY_SYM_TAB',
           'TERMKEY_SYM_DEL', 'TERMKEY_SYM_CLOSE',
           'TERMKEY_SYM_SELECT', 'TERMKEY_SYM_EXIT', 'termkey',
           'TERMKEY_SYM_FIND', 'TERMKEY_TYPE_UNICODE',
           'TERMKEY_SYM_ENTER', 'TERMKEY_SYM_KPCOMMA',
           'waitkey']
