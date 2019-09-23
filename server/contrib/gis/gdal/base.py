from server.contrib.gis.gdal.error import GDALException
from server.contrib.gis.ptr import CPointerBase


class GDALBase(CPointerBase):
    null_ptr_exception_class = GDALException
