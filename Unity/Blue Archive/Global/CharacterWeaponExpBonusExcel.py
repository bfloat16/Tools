# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Global

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterWeaponExpBonusExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterWeaponExpBonusExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterWeaponExpBonusExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterWeaponExpBonusExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterWeaponExpBonusExcel
    def WeaponType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterWeaponExpBonusExcel
    def WeaponExpGrowthA(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterWeaponExpBonusExcel
    def WeaponExpGrowthB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterWeaponExpBonusExcel
    def WeaponExpGrowthC(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CharacterWeaponExpBonusExcel
    def WeaponExpGrowthZ(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def CharacterWeaponExpBonusExcelStart(builder):
    builder.StartObject(5)

def Start(builder):
    CharacterWeaponExpBonusExcelStart(builder)

def CharacterWeaponExpBonusExcelAddWeaponType(builder, weaponType):
    builder.PrependInt32Slot(0, weaponType, 0)

def AddWeaponType(builder, weaponType):
    CharacterWeaponExpBonusExcelAddWeaponType(builder, weaponType)

def CharacterWeaponExpBonusExcelAddWeaponExpGrowthA(builder, weaponExpGrowthA):
    builder.PrependInt32Slot(1, weaponExpGrowthA, 0)

def AddWeaponExpGrowthA(builder, weaponExpGrowthA):
    CharacterWeaponExpBonusExcelAddWeaponExpGrowthA(builder, weaponExpGrowthA)

def CharacterWeaponExpBonusExcelAddWeaponExpGrowthB(builder, weaponExpGrowthB):
    builder.PrependInt32Slot(2, weaponExpGrowthB, 0)

def AddWeaponExpGrowthB(builder, weaponExpGrowthB):
    CharacterWeaponExpBonusExcelAddWeaponExpGrowthB(builder, weaponExpGrowthB)

def CharacterWeaponExpBonusExcelAddWeaponExpGrowthC(builder, weaponExpGrowthC):
    builder.PrependInt32Slot(3, weaponExpGrowthC, 0)

def AddWeaponExpGrowthC(builder, weaponExpGrowthC):
    CharacterWeaponExpBonusExcelAddWeaponExpGrowthC(builder, weaponExpGrowthC)

def CharacterWeaponExpBonusExcelAddWeaponExpGrowthZ(builder, weaponExpGrowthZ):
    builder.PrependInt32Slot(4, weaponExpGrowthZ, 0)

def AddWeaponExpGrowthZ(builder, weaponExpGrowthZ):
    CharacterWeaponExpBonusExcelAddWeaponExpGrowthZ(builder, weaponExpGrowthZ)

def CharacterWeaponExpBonusExcelEnd(builder):
    return builder.EndObject()

def End(builder):
    return CharacterWeaponExpBonusExcelEnd(builder)
