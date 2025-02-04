"""
This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from typing import Iterable, overload

from zospy.api._ZOSAPI.Editors.LDE import ILDERow
from zospy.api._ZOSAPI.Tools.General import IDataDictionary

__all__ = (
    "DrawingCementData",
    "DrawingCementData",
    "DrawingComponentData",
    "DrawingComponentData",
    "DrawingMaterialData",
    "DrawingMaterialData",
    "DrawingSurfaceData",
    "DrawingSurfaceData",
    "LMXF_GeneralSettings",
    "LMXF_GeneralSettings",
    "LMXF_NscConfigData",
    "LMXF_NscConfigData",
    "LMXF_NscData",
    "LMXF_NscData",
    "LMXF_NscSourceData",
    "LMXF_NscSourceData",
    "LMXF_OpticalAxisSurfaceData",
    "LMXF_OpticalAxisSurfaceData",
    "LMXF_Platforms",
    "LMXF_SeqConfigData",
    "LMXF_SeqConfigData",
    "LMXF_SeqData",
    "LMXF_SeqData",
    "LMXF_Wrapper",
    "LMXF_Wrapper",
)

class DrawingCementData:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, cement: DrawingCementData): ...
    @property
    def CementType(self) -> str: ...
    @property
    def CementWedge(self) -> Nullable: ...
    @property
    def LocalizedImpTol(self) -> Nullable: ...
    @property
    def RotationalInvariant(self) -> Nullable: ...
    @property
    def SurfaceImpTol(self) -> Nullable: ...
    @property
    def TransmitWavefront(self) -> Nullable: ...
    @CementType.setter
    def CementType(self, value: str) -> None: ...
    @CementWedge.setter
    def CementWedge(self, value: Nullable) -> None: ...
    @LocalizedImpTol.setter
    def LocalizedImpTol(self, value: Nullable) -> None: ...
    @RotationalInvariant.setter
    def RotationalInvariant(self, value: Nullable) -> None: ...
    @SurfaceImpTol.setter
    def SurfaceImpTol(self, value: Nullable) -> None: ...
    @TransmitWavefront.setter
    def TransmitWavefront(self, value: Nullable) -> None: ...

class DrawingComponentData:
    @overload
    def __init__(self, isSequentialMode: bool): ...
    @overload
    def __init__(self, component: DrawingComponentData, isSequentialMode: bool): ...
    @property
    def BackSurface(self) -> DrawingSurfaceData: ...
    @property
    def BackSurfaceNumber(self) -> int: ...
    @property
    def CementData(self) -> DrawingCementData: ...
    @property
    def ElementType(self) -> int: ...
    @property
    def FrontSurface(self) -> DrawingSurfaceData: ...
    @property
    def FrontSurfaceNumber(self) -> int: ...
    @property
    def IsDrawingInputsSupportedForBackSurface(self) -> bool: ...
    @property
    def IsDrawingInputsSupportedForFrontSurface(self) -> bool: ...
    @property
    def IsLeadElement(self) -> bool: ...
    @property
    def Material(self) -> DrawingMaterialData: ...
    @property
    def ObjectNumber(self) -> int: ...
    @BackSurface.setter
    def BackSurface(self, value: DrawingSurfaceData) -> None: ...
    @BackSurfaceNumber.setter
    def BackSurfaceNumber(self, value: int) -> None: ...
    @CementData.setter
    def CementData(self, value: DrawingCementData) -> None: ...
    @ElementType.setter
    def ElementType(self, value: int) -> None: ...
    @FrontSurface.setter
    def FrontSurface(self, value: DrawingSurfaceData) -> None: ...
    @FrontSurfaceNumber.setter
    def FrontSurfaceNumber(self, value: int) -> None: ...
    @IsLeadElement.setter
    def IsLeadElement(self, value: bool) -> None: ...
    @Material.setter
    def Material(self, value: DrawingMaterialData) -> None: ...
    @ObjectNumber.setter
    def ObjectNumber(self, value: int) -> None: ...

class DrawingMaterialData:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, material: DrawingMaterialData): ...
    @property
    def AbbeNumber(self) -> Nullable: ...
    @property
    def AbbeTolerance(self) -> Nullable: ...
    @property
    def BubblesInclusions(self) -> str: ...
    @property
    def Dig(self) -> Nullable: ...
    @property
    def IndexOfRefraction(self) -> Nullable: ...
    @property
    def IndexTolerance(self) -> Nullable: ...
    @property
    def InhomogeneityStriae(self) -> str: ...
    @property
    def Material(self) -> str: ...
    @property
    def ReferenceWL(self) -> Nullable: ...
    @property
    def Scratch(self) -> Nullable: ...
    @property
    def StressBirefringence(self) -> Nullable: ...
    @property
    def TestWavelengthNM(self) -> Nullable: ...
    @property
    def Thickness(self) -> Nullable: ...
    @property
    def ThicknessTolerance(self) -> Nullable: ...
    @property
    def TransmittedWavefront(self) -> str: ...
    @property
    def WavefrontDeformTol(self) -> str: ...
    @AbbeNumber.setter
    def AbbeNumber(self, value: Nullable) -> None: ...
    @AbbeTolerance.setter
    def AbbeTolerance(self, value: Nullable) -> None: ...
    @BubblesInclusions.setter
    def BubblesInclusions(self, value: str) -> None: ...
    @Dig.setter
    def Dig(self, value: Nullable) -> None: ...
    @IndexOfRefraction.setter
    def IndexOfRefraction(self, value: Nullable) -> None: ...
    @IndexTolerance.setter
    def IndexTolerance(self, value: Nullable) -> None: ...
    @InhomogeneityStriae.setter
    def InhomogeneityStriae(self, value: str) -> None: ...
    @Material.setter
    def Material(self, value: str) -> None: ...
    @ReferenceWL.setter
    def ReferenceWL(self, value: Nullable) -> None: ...
    @Scratch.setter
    def Scratch(self, value: Nullable) -> None: ...
    @StressBirefringence.setter
    def StressBirefringence(self, value: Nullable) -> None: ...
    @TestWavelengthNM.setter
    def TestWavelengthNM(self, value: Nullable) -> None: ...
    @Thickness.setter
    def Thickness(self, value: Nullable) -> None: ...
    @ThicknessTolerance.setter
    def ThicknessTolerance(self, value: Nullable) -> None: ...
    @TransmittedWavefront.setter
    def TransmittedWavefront(self, value: str) -> None: ...
    @WavefrontDeformTol.setter
    def WavefrontDeformTol(self, value: str) -> None: ...

class DrawingSurfaceData:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, data: DrawingSurfaceData): ...
    def CreateRange(rMin: float, rMax: float, numR: int) -> Iterable[float]: ...
    @property
    def AsphereCoefficients(self) -> list[float]: ...
    @property
    def CentrationDecentration(self) -> Nullable: ...
    @property
    def ClearAperture(self) -> Nullable: ...
    @property
    def ClearApertureTolerance(self) -> Nullable: ...
    @property
    def Coating(self) -> str: ...
    @property
    def Conic(self) -> Nullable: ...
    @property
    def FTWMax(self) -> Nullable: ...
    @property
    def FTWMin(self) -> Nullable: ...
    @property
    def FTWPct(self) -> Nullable: ...
    @property
    def ImperfectionTolerance(self) -> str: ...
    @property
    def IrregularityFormError(self) -> str: ...
    @property
    def IsAspheric(self) -> bool: ...
    @property
    def IsDrawingInputsSupported(self) -> bool: ...
    @property
    def LaserPowerDamage(self) -> str: ...
    @property
    def PaintNotes(self) -> str: ...
    @property
    def PowerIrr(self) -> str: ...
    @property
    def ProtectionChamfer(self) -> Nullable: ...
    @property
    def Radius(self) -> Nullable: ...
    @property
    def RadiusTolerance(self) -> Nullable: ...
    @property
    def ReferenceWavelengthNM(self) -> Nullable: ...
    @property
    def SagData(self) -> list[float]: ...
    @property
    def SagDataSemiDiameter(self) -> Nullable: ...
    @property
    def SagTable(self) -> list[list[float]]: ...
    @property
    def SagTableHeight(self) -> Nullable: ...
    @property
    def SagTableWidth(self) -> Nullable: ...
    @property
    def SlopeError(self) -> Nullable: ...
    @property
    def SurfaceName(self) -> str: ...
    @property
    def SurfaceTexture(self) -> str: ...
    @property
    def SurfaceType(self) -> str: ...
    @property
    def TiltWedge(self) -> Nullable: ...
    @property
    def VertexRadius(self) -> Nullable: ...
    @property
    def VertexRadiusTolerance(self) -> Nullable: ...
    def GetAsphericSag(self, radii: Iterable[float]) -> List: ...
    def GetAsphericSagAtRadius(self, r: float) -> float: ...
    def GetInvariantSurfaceTypeName(surface: ILDERow) -> str: ...
    @AsphereCoefficients.setter
    def AsphereCoefficients(self, value: list[float]) -> None: ...
    @CentrationDecentration.setter
    def CentrationDecentration(self, value: Nullable) -> None: ...
    @ClearAperture.setter
    def ClearAperture(self, value: Nullable) -> None: ...
    @ClearApertureTolerance.setter
    def ClearApertureTolerance(self, value: Nullable) -> None: ...
    @Coating.setter
    def Coating(self, value: str) -> None: ...
    @Conic.setter
    def Conic(self, value: Nullable) -> None: ...
    @FTWMax.setter
    def FTWMax(self, value: Nullable) -> None: ...
    @FTWMin.setter
    def FTWMin(self, value: Nullable) -> None: ...
    @FTWPct.setter
    def FTWPct(self, value: Nullable) -> None: ...
    @ImperfectionTolerance.setter
    def ImperfectionTolerance(self, value: str) -> None: ...
    @IrregularityFormError.setter
    def IrregularityFormError(self, value: str) -> None: ...
    @LaserPowerDamage.setter
    def LaserPowerDamage(self, value: str) -> None: ...
    @PaintNotes.setter
    def PaintNotes(self, value: str) -> None: ...
    @PowerIrr.setter
    def PowerIrr(self, value: str) -> None: ...
    @ProtectionChamfer.setter
    def ProtectionChamfer(self, value: Nullable) -> None: ...
    @Radius.setter
    def Radius(self, value: Nullable) -> None: ...
    @RadiusTolerance.setter
    def RadiusTolerance(self, value: Nullable) -> None: ...
    @ReferenceWavelengthNM.setter
    def ReferenceWavelengthNM(self, value: Nullable) -> None: ...
    @SagData.setter
    def SagData(self, value: list[float]) -> None: ...
    @SagDataSemiDiameter.setter
    def SagDataSemiDiameter(self, value: Nullable) -> None: ...
    @SagTable.setter
    def SagTable(self, value: list[list[float]]) -> None: ...
    @SagTableHeight.setter
    def SagTableHeight(self, value: Nullable) -> None: ...
    @SagTableWidth.setter
    def SagTableWidth(self, value: Nullable) -> None: ...
    @SlopeError.setter
    def SlopeError(self, value: Nullable) -> None: ...
    @SurfaceName.setter
    def SurfaceName(self, value: str) -> None: ...
    @SurfaceTexture.setter
    def SurfaceTexture(self, value: str) -> None: ...
    @SurfaceType.setter
    def SurfaceType(self, value: str) -> None: ...
    @TiltWedge.setter
    def TiltWedge(self, value: Nullable) -> None: ...
    @VertexRadius.setter
    def VertexRadius(self, value: Nullable) -> None: ...
    @VertexRadiusTolerance.setter
    def VertexRadiusTolerance(self, value: Nullable) -> None: ...

class LMXF_GeneralSettings:
    def __init__(self): ...
    @property
    def ConvertStopToNSCAperture(self) -> bool: ...
    @property
    def IncludeScatter(self) -> bool: ...
    @property
    def IncludeSplitting(self) -> bool: ...
    @property
    def IsEditable(self) -> bool: ...
    @property
    def Notes(self) -> str: ...
    @property
    def Precision(self) -> int: ...
    @property
    def StopMechanicalHalfWidth(self) -> float: ...
    @property
    def TargetPlatform(self) -> LMXF_Platforms: ...
    @ConvertStopToNSCAperture.setter
    def ConvertStopToNSCAperture(self, value: bool) -> None: ...
    @IncludeScatter.setter
    def IncludeScatter(self, value: bool) -> None: ...
    @IncludeSplitting.setter
    def IncludeSplitting(self, value: bool) -> None: ...
    @IsEditable.setter
    def IsEditable(self, value: bool) -> None: ...
    @Notes.setter
    def Notes(self, value: str) -> None: ...
    @Precision.setter
    def Precision(self, value: int) -> None: ...
    @StopMechanicalHalfWidth.setter
    def StopMechanicalHalfWidth(self, value: float) -> None: ...
    @TargetPlatform.setter
    def TargetPlatform(self, value: LMXF_Platforms) -> None: ...

class LMXF_NscConfigData:
    def __init__(self): ...
    @property
    def ComponentObjects(self) -> list[int]: ...
    @property
    def ComponentPositions(self) -> list[list[float]]: ...
    @property
    def DrawingData(self) -> list[DrawingComponentData]: ...
    @property
    def NscSourceData(self) -> LMXF_NscSourceData: ...
    @property
    def OriginalConfigNumber(self) -> int: ...
    @ComponentObjects.setter
    def ComponentObjects(self, value: list[int]) -> None: ...
    @ComponentPositions.setter
    def ComponentPositions(self, value: list[list[float]]) -> None: ...
    @DrawingData.setter
    def DrawingData(self, value: list[DrawingComponentData]) -> None: ...
    @NscSourceData.setter
    def NscSourceData(self, value: LMXF_NscSourceData) -> None: ...
    @OriginalConfigNumber.setter
    def OriginalConfigNumber(self, value: int) -> None: ...

class LMXF_NscData:
    def __init__(self): ...
    @property
    def ConfigData(self) -> list[LMXF_NscConfigData]: ...
    @property
    def IsNscSource(self) -> bool: ...
    @property
    def NSCFileKey(self) -> str: ...
    @property
    def NSCFileName(self) -> str: ...
    @property
    def StopObjectFace(self) -> int: ...
    @property
    def StopObjectNumber(self) -> int: ...
    @ConfigData.setter
    def ConfigData(self, value: list[LMXF_NscConfigData]) -> None: ...
    @IsNscSource.setter
    def IsNscSource(self, value: bool) -> None: ...
    @NSCFileKey.setter
    def NSCFileKey(self, value: str) -> None: ...
    @NSCFileName.setter
    def NSCFileName(self, value: str) -> None: ...
    @StopObjectFace.setter
    def StopObjectFace(self, value: int) -> None: ...
    @StopObjectNumber.setter
    def StopObjectNumber(self, value: int) -> None: ...

class LMXF_NscSourceData:
    def __init__(self): ...
    @property
    def DetectorDataKeys(self) -> list[str]: ...
    @property
    def DetectorObjects(self) -> list[int]: ...
    @property
    def IntendedPathFlux(self) -> list[float]: ...
    @property
    def IntendedPaths(self) -> list[list[int]]: ...
    @property
    def NscMtfData(self) -> list[list[float]]: ...
    @property
    def NscSpotImageKeys(self) -> list[str]: ...
    @property
    def NscSpotSizes(self) -> list[float]: ...
    @property
    def SourceObjects(self) -> list[int]: ...
    @property
    def TotalFlux(self) -> float: ...
    @DetectorDataKeys.setter
    def DetectorDataKeys(self, value: list[str]) -> None: ...
    @DetectorObjects.setter
    def DetectorObjects(self, value: list[int]) -> None: ...
    @IntendedPathFlux.setter
    def IntendedPathFlux(self, value: list[float]) -> None: ...
    @IntendedPaths.setter
    def IntendedPaths(self, value: list[list[int]]) -> None: ...
    @NscMtfData.setter
    def NscMtfData(self, value: list[list[float]]) -> None: ...
    @NscSpotImageKeys.setter
    def NscSpotImageKeys(self, value: list[str]) -> None: ...
    @NscSpotSizes.setter
    def NscSpotSizes(self, value: list[float]) -> None: ...
    @SourceObjects.setter
    def SourceObjects(self, value: list[int]) -> None: ...
    @TotalFlux.setter
    def TotalFlux(self, value: float) -> None: ...

class LMXF_OpticalAxisSurfaceData:
    @property
    def AreCoordinatesGlobal(self) -> bool: ...
    @property
    def ErrorCode(self) -> int: ...
    @property
    def Nx(self) -> float: ...
    @property
    def Ny(self) -> float: ...
    @property
    def Nz(self) -> float: ...
    @property
    def SurfaceNumber(self) -> int: ...
    @property
    def VignetteCode(self) -> int: ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...
    @property
    def Z(self) -> float: ...
    @AreCoordinatesGlobal.setter
    def AreCoordinatesGlobal(self, value: bool) -> None: ...
    @ErrorCode.setter
    def ErrorCode(self, value: int) -> None: ...
    @Nx.setter
    def Nx(self, value: float) -> None: ...
    @Ny.setter
    def Ny(self, value: float) -> None: ...
    @Nz.setter
    def Nz(self, value: float) -> None: ...
    @SurfaceNumber.setter
    def SurfaceNumber(self, value: int) -> None: ...
    @VignetteCode.setter
    def VignetteCode(self, value: int) -> None: ...
    @X.setter
    def X(self, value: float) -> None: ...
    @Y.setter
    def Y(self, value: float) -> None: ...
    @Z.setter
    def Z(self, value: float) -> None: ...

class LMXF_Platforms:
    Unknown = 0
    SolidWorks = 1
    Creo = 2

class LMXF_SeqConfigData:
    def __init__(self): ...
    @property
    def ComponentPositions(self) -> list[list[float]]: ...
    @property
    def ComponentSurfaces(self) -> list[int]: ...
    @property
    def CrsFileKey(self) -> str: ...
    @property
    def DetectorDataKeys(self) -> list[str]: ...
    @property
    def DetectorObjects(self) -> list[int]: ...
    @property
    def FieldNumbers(self) -> list[int]: ...
    @property
    def FullFieldKey(self) -> str: ...
    @property
    def IntendedPathFlux(self) -> list[float]: ...
    @property
    def IntendedPaths(self) -> list[list[int]]: ...
    @property
    def NscMtfData(self) -> list[list[float]]: ...
    @property
    def NscSpotImageKeys(self) -> list[str]: ...
    @property
    def NscSpotSizes(self) -> list[float]: ...
    @property
    def OpticalAxisData(self) -> list[LMXF_OpticalAxisSurfaceData]: ...
    @property
    def OriginalConfigNumber(self) -> int: ...
    @property
    def SeqMtfData(self) -> list[list[float]]: ...
    @property
    def SeqSpotImageKeys(self) -> list[str]: ...
    @property
    def SeqSpotSizes(self) -> list[float]: ...
    @property
    def SourceObjects(self) -> list[int]: ...
    @property
    def TotalFlux(self) -> float: ...
    @property
    def ZrdFileKey(self) -> str: ...
    @ComponentPositions.setter
    def ComponentPositions(self, value: list[list[float]]) -> None: ...
    @ComponentSurfaces.setter
    def ComponentSurfaces(self, value: list[int]) -> None: ...
    @CrsFileKey.setter
    def CrsFileKey(self, value: str) -> None: ...
    @DetectorDataKeys.setter
    def DetectorDataKeys(self, value: list[str]) -> None: ...
    @DetectorObjects.setter
    def DetectorObjects(self, value: list[int]) -> None: ...
    @FieldNumbers.setter
    def FieldNumbers(self, value: list[int]) -> None: ...
    @FullFieldKey.setter
    def FullFieldKey(self, value: str) -> None: ...
    @IntendedPathFlux.setter
    def IntendedPathFlux(self, value: list[float]) -> None: ...
    @IntendedPaths.setter
    def IntendedPaths(self, value: list[list[int]]) -> None: ...
    @NscMtfData.setter
    def NscMtfData(self, value: list[list[float]]) -> None: ...
    @NscSpotImageKeys.setter
    def NscSpotImageKeys(self, value: list[str]) -> None: ...
    @NscSpotSizes.setter
    def NscSpotSizes(self, value: list[float]) -> None: ...
    @OpticalAxisData.setter
    def OpticalAxisData(self, value: list[LMXF_OpticalAxisSurfaceData]) -> None: ...
    @OriginalConfigNumber.setter
    def OriginalConfigNumber(self, value: int) -> None: ...
    @SeqMtfData.setter
    def SeqMtfData(self, value: list[list[float]]) -> None: ...
    @SeqSpotImageKeys.setter
    def SeqSpotImageKeys(self, value: list[str]) -> None: ...
    @SeqSpotSizes.setter
    def SeqSpotSizes(self, value: list[float]) -> None: ...
    @SourceObjects.setter
    def SourceObjects(self, value: list[int]) -> None: ...
    @TotalFlux.setter
    def TotalFlux(self, value: float) -> None: ...
    @ZrdFileKey.setter
    def ZrdFileKey(self, value: str) -> None: ...

class LMXF_SeqData:
    def __init__(self): ...
    @property
    def ConfigData(self) -> list[LMXF_SeqConfigData]: ...
    @property
    def CriticalRayAngleTolerance(self) -> float: ...
    @property
    def CriticalRayPositionTolerance(self) -> float: ...
    @property
    def DeltaBeamClipPct(self) -> float: ...
    @property
    def DeltaImgContPct(self) -> float: ...
    @property
    def DeltaSpotPct(self) -> float: ...
    @property
    def DeltaSpotUM(self) -> float: ...
    @property
    def DeltaSpotUsePct(self) -> bool: ...
    @property
    def IsCopiedData(self) -> bool: ...
    @property
    def MaxMtfFreq(self) -> float: ...
    @property
    def NumberOfAnalysisRays(self) -> int: ...
    @property
    def SEQFileKey(self) -> str: ...
    @property
    def SEQFileName(self) -> str: ...
    @ConfigData.setter
    def ConfigData(self, value: list[LMXF_SeqConfigData]) -> None: ...
    @CriticalRayAngleTolerance.setter
    def CriticalRayAngleTolerance(self, value: float) -> None: ...
    @CriticalRayPositionTolerance.setter
    def CriticalRayPositionTolerance(self, value: float) -> None: ...
    @DeltaBeamClipPct.setter
    def DeltaBeamClipPct(self, value: float) -> None: ...
    @DeltaImgContPct.setter
    def DeltaImgContPct(self, value: float) -> None: ...
    @DeltaSpotPct.setter
    def DeltaSpotPct(self, value: float) -> None: ...
    @DeltaSpotUM.setter
    def DeltaSpotUM(self, value: float) -> None: ...
    @DeltaSpotUsePct.setter
    def DeltaSpotUsePct(self, value: bool) -> None: ...
    @IsCopiedData.setter
    def IsCopiedData(self, value: bool) -> None: ...
    @MaxMtfFreq.setter
    def MaxMtfFreq(self, value: float) -> None: ...
    @NumberOfAnalysisRays.setter
    def NumberOfAnalysisRays(self, value: int) -> None: ...
    @SEQFileKey.setter
    def SEQFileKey(self, value: str) -> None: ...
    @SEQFileName.setter
    def SEQFileName(self, value: str) -> None: ...

class LMXF_Wrapper:
    def __init__(self, dataFile: IDataDictionary): ...
    def GetGeneralSettings(self) -> LMXF_GeneralSettings: ...
    def GetNscData(self) -> LMXF_NscData: ...
    def GetSeqData(self) -> LMXF_SeqData: ...
    def SaveConfigCRS(self, cfgData: LMXF_SeqConfigData, fileName: str) -> None: ...
    def SaveConfigDetector(self, cfgData: LMXF_SeqConfigData, fieldIdx: int, fileName: str) -> None: ...
    def SaveConfigFullFieldDetector(self, cfgData: LMXF_SeqConfigData, fileName: str) -> None: ...
    def SaveConfigZRD(self, cfgData: LMXF_SeqConfigData, fileName: str) -> None: ...
    def SaveNscZAR(self, nscData: LMXF_NscData, fileName: str) -> bool: ...
    def SaveSeqZAR(self, seqData: LMXF_SeqData, fileName: str) -> None: ...
    def SaveSpotFile(self, cfgData: LMXF_SeqConfigData, seqFile: bool, fieldIdx: int, fileName: str) -> None: ...
