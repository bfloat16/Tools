# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GroundNodeLayerFlat(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GroundNodeLayerFlat()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGroundNodeLayerFlat(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GroundNodeLayerFlat
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GroundNodeLayerFlat
    def Layers(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # GroundNodeLayerFlat
    def LayersAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int8Flags, o)
        return 0

    # GroundNodeLayerFlat
    def LayersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GroundNodeLayerFlat
    def LayersIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def GroundNodeLayerFlatStart(builder):
    builder.StartObject(1)

def Start(builder):
    GroundNodeLayerFlatStart(builder)

def GroundNodeLayerFlatAddLayers(builder, layers):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(layers), 0)

def AddLayers(builder, layers):
    GroundNodeLayerFlatAddLayers(builder, layers)

def GroundNodeLayerFlatStartLayersVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartLayersVector(builder, numElems):
    return GroundNodeLayerFlatStartLayersVector(builder, numElems)

def GroundNodeLayerFlatEnd(builder):
    return builder.EndObject()

def End(builder):
    return GroundNodeLayerFlatEnd(builder)
