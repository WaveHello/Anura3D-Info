# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
fndn_axi_NAMC_v1_3_MeshData_00 = LegacyVTKReader(registrationName='Fndn_axi_NAMC_v1_3_MeshData_00*', FileNames=['C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MeshData_001000001.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MeshData_001000013.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MeshData_002000017.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MeshData_003000018.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MeshData_004000020.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MeshData_005000017.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MeshData_006000006.vtk'])

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# create a new 'Legacy VTK Reader'
fndn_axi_NAMC_v1_3_MPScalar_00 = LegacyVTKReader(registrationName='Fndn_axi_NAMC_v1_3_MPScalar_00*', FileNames=['C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPScalar_001000001.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPScalar_001000013.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPScalar_002000017.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPScalar_003000018.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPScalar_004000020.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPScalar_005000017.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPScalar_006000006.vtk'])

# create a new 'Legacy VTK Reader'
fndn_axi_NAMC_v1_3_MPTensor_00 = LegacyVTKReader(registrationName='Fndn_axi_NAMC_v1_3_MPTensor_00*', FileNames=['C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPTensor_001000001.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPTensor_001000013.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPTensor_002000017.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPTensor_003000018.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPTensor_004000020.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPTensor_005000017.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPTensor_006000006.vtk'])

# create a new 'Legacy VTK Reader'
fndn_axi_NAMC_v1_3_MPVector_00 = LegacyVTKReader(registrationName='Fndn_axi_NAMC_v1_3_MPVector_00*', FileNames=['C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPVector_001000001.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPVector_001000013.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPVector_002000017.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPVector_003000018.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPVector_004000020.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPVector_005000017.vtk', 'C:\\Geotech_Research\\Tutorial_Models\\Foundation_Models\\inital_velocity\\2D_axisymmetric\\OS_NAMC\\Fndn_axi_NAMC_v1_3.A3D\\Fndn_axi_NAMC_v1_3_MPVector_006000006.vtk'])

# get active view
renderView3 = GetActiveViewOrCreate('RenderView')

# show data in view
fndn_axi_NAMC_v1_3_MeshData_00Display = Show(fndn_axi_NAMC_v1_3_MeshData_00, renderView3, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'active_elements'
active_elementsLUT = GetColorTransferFunction('active_elements')

# get opacity transfer function/opacity map for 'active_elements'
active_elementsPWF = GetOpacityTransferFunction('active_elements')

# trace defaults for the display properties.
fndn_axi_NAMC_v1_3_MeshData_00Display.Selection = None
fndn_axi_NAMC_v1_3_MeshData_00Display.Representation = 'Surface'
fndn_axi_NAMC_v1_3_MeshData_00Display.ColorArrayName = ['CELLS', 'active_elements']
fndn_axi_NAMC_v1_3_MeshData_00Display.LookupTable = active_elementsLUT
fndn_axi_NAMC_v1_3_MeshData_00Display.MapScalars = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.MultiComponentsMapping = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.InterpolateScalarsBeforeMapping = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.Opacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PointSize = 2.0
fndn_axi_NAMC_v1_3_MeshData_00Display.LineWidth = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.RenderLinesAsTubes = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.RenderPointsAsSpheres = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.Interpolation = 'Gouraud'
fndn_axi_NAMC_v1_3_MeshData_00Display.Specular = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.SpecularColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.SpecularPower = 100.0
fndn_axi_NAMC_v1_3_MeshData_00Display.Luminosity = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.Ambient = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.Diffuse = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.Roughness = 0.3
fndn_axi_NAMC_v1_3_MeshData_00Display.Metallic = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.EdgeTint = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.Anisotropy = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.AnisotropyRotation = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.BaseIOR = 1.5
fndn_axi_NAMC_v1_3_MeshData_00Display.CoatStrength = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.CoatIOR = 2.0
fndn_axi_NAMC_v1_3_MeshData_00Display.CoatRoughness = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.CoatColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectTCoordArray = 'None'
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectNormalArray = 'None'
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectTangentArray = 'None'
fndn_axi_NAMC_v1_3_MeshData_00Display.Texture = None
fndn_axi_NAMC_v1_3_MeshData_00Display.RepeatTextures = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.InterpolateTextures = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.SeamlessU = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.SeamlessV = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.UseMipmapTextures = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.ShowTexturesOnBackface = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.BaseColorTexture = None
fndn_axi_NAMC_v1_3_MeshData_00Display.NormalTexture = None
fndn_axi_NAMC_v1_3_MeshData_00Display.NormalScale = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.CoatNormalTexture = None
fndn_axi_NAMC_v1_3_MeshData_00Display.CoatNormalScale = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.MaterialTexture = None
fndn_axi_NAMC_v1_3_MeshData_00Display.OcclusionStrength = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.AnisotropyTexture = None
fndn_axi_NAMC_v1_3_MeshData_00Display.EmissiveTexture = None
fndn_axi_NAMC_v1_3_MeshData_00Display.EmissiveFactor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.FlipTextures = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.BackfaceRepresentation = 'Follow Frontface'
fndn_axi_NAMC_v1_3_MeshData_00Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.BackfaceOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.Position = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.Scale = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.Orientation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.Origin = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
fndn_axi_NAMC_v1_3_MeshData_00Display.Pickable = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.Triangulate = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.UseShaderReplacements = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.ShaderReplacements = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.NonlinearSubdivisionLevel = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.UseDataPartitions = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.OSPRayUseScaleArray = 'All Approximate'
fndn_axi_NAMC_v1_3_MeshData_00Display.OSPRayScaleArray = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.OSPRayScaleFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MeshData_00Display.OSPRayMaterial = 'None'
fndn_axi_NAMC_v1_3_MeshData_00Display.BlockSelectors = ['/']
fndn_axi_NAMC_v1_3_MeshData_00Display.BlockColors = []
fndn_axi_NAMC_v1_3_MeshData_00Display.BlockOpacities = []
fndn_axi_NAMC_v1_3_MeshData_00Display.Orient = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.OrientationMode = 'Direction'
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectOrientationVectors = 'None'
fndn_axi_NAMC_v1_3_MeshData_00Display.Scaling = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.ScaleMode = 'No Data Scaling Off'
fndn_axi_NAMC_v1_3_MeshData_00Display.ScaleFactor = 1.5
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectScaleArray = 'active_elements'
fndn_axi_NAMC_v1_3_MeshData_00Display.GlyphType = 'Arrow'
fndn_axi_NAMC_v1_3_MeshData_00Display.UseGlyphTable = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.GlyphTableIndexArray = 'active_elements'
fndn_axi_NAMC_v1_3_MeshData_00Display.UseCompositeGlyphTable = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.UseGlyphCullingAndLOD = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.LODValues = []
fndn_axi_NAMC_v1_3_MeshData_00Display.ColorByLODIndex = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.GaussianRadius = 0.075
fndn_axi_NAMC_v1_3_MeshData_00Display.ShaderPreset = 'Sphere'
fndn_axi_NAMC_v1_3_MeshData_00Display.CustomTriangleScale = 3
fndn_axi_NAMC_v1_3_MeshData_00Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
fndn_axi_NAMC_v1_3_MeshData_00Display.Emissive = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.ScaleByArray = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.SetScaleArray = [None, '']
fndn_axi_NAMC_v1_3_MeshData_00Display.ScaleArrayComponent = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.UseScaleFunction = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.ScaleTransferFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MeshData_00Display.OpacityByArray = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.OpacityArray = [None, '']
fndn_axi_NAMC_v1_3_MeshData_00Display.OpacityArrayComponent = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.OpacityTransferFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid = 'GridAxesRepresentation'
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionCellLabelBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionCellLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionCellLabelFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionCellLabelFontSize = 18
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionCellLabelItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionCellLabelJustification = 'Left'
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionCellLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionCellLabelShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionPointLabelBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionPointLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionPointLabelFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionPointLabelFontSize = 18
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionPointLabelItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionPointLabelJustification = 'Left'
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionPointLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectionPointLabelShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes = 'PolarAxesRepresentation'
fndn_axi_NAMC_v1_3_MeshData_00Display.ScalarOpacityFunction = active_elementsPWF
fndn_axi_NAMC_v1_3_MeshData_00Display.ScalarOpacityUnitDistance = 1.6599031182247197
fndn_axi_NAMC_v1_3_MeshData_00Display.UseSeparateOpacityArray = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.OpacityArrayName = ['CELLS', 'active_elements']
fndn_axi_NAMC_v1_3_MeshData_00Display.OpacityComponent = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.SelectMapper = 'Projected tetra'
fndn_axi_NAMC_v1_3_MeshData_00Display.SamplingDimensions = [128, 128, 128]
fndn_axi_NAMC_v1_3_MeshData_00Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fndn_axi_NAMC_v1_3_MeshData_00Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
fndn_axi_NAMC_v1_3_MeshData_00Display.GlyphType.TipResolution = 6
fndn_axi_NAMC_v1_3_MeshData_00Display.GlyphType.TipRadius = 0.1
fndn_axi_NAMC_v1_3_MeshData_00Display.GlyphType.TipLength = 0.35
fndn_axi_NAMC_v1_3_MeshData_00Display.GlyphType.ShaftResolution = 6
fndn_axi_NAMC_v1_3_MeshData_00Display.GlyphType.ShaftRadius = 0.03
fndn_axi_NAMC_v1_3_MeshData_00Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fndn_axi_NAMC_v1_3_MeshData_00Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fndn_axi_NAMC_v1_3_MeshData_00Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XTitle = 'X Axis'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YTitle = 'Y Axis'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZTitle = 'Z Axis'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XTitleFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XTitleBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XTitleItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XTitleFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XTitleShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YTitleFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YTitleBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YTitleItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YTitleFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YTitleShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZTitleFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZTitleBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZTitleItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZTitleFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZTitleShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.FacesToRender = 63
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.CullBackface = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.CullFrontface = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ShowGrid = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ShowEdges = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ShowTicks = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.AxesToLabel = 63
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XLabelFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XLabelBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XLabelItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XLabelFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XLabelShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YLabelFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YLabelBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YLabelItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YLabelFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YLabelShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZLabelFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZLabelBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZLabelItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZLabelFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZLabelShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XAxisPrecision = 2
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.XAxisLabels = []
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YAxisPrecision = 2
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.YAxisLabels = []
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZAxisPrecision = 2
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.ZAxisLabels = []
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.UseCustomBounds = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.Visibility = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.EnableCustomRange = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.CustomRange = [0.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.RadialAxesVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.DrawRadialGridlines = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarArcsVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.DrawPolarArcsGridlines = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.NumberOfRadialAxes = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.AutoSubdividePolarAxis = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.NumberOfPolarAxis = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.MinimumRadius = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.MinimumAngle = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.MaximumAngle = 90.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.Ratio = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitleVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarLabelVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.RadialLabelVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.RadialLabelLocation = 'Bottom'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.RadialUnitsVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.ScreenSize = 10.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitleFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitleBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitleItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitleShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTitleFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisLabelFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisLabelBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisLabelItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisLabelShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisLabelFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisTextFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisTextBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisTextItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisTextShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisTextFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SecondaryRadialAxesTextBold = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.EnableDistanceLOD = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.DistanceLODThreshold = 0.7
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.EnableViewAngleLOD = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.ViewAngleLODThreshold = 0.7
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarTicksVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.TickLocation = 'Both'
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.AxisTickVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.AxisMinorTickVisibility = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.ArcTickVisibility = 1
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.ArcMinorTickVisibility = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.DeltaAngleMajor = 10.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.DeltaAngleMinor = 5.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.ArcMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.ArcTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.ArcMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.ArcTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.Use2DMode = 0
fndn_axi_NAMC_v1_3_MeshData_00Display.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView3.ResetCamera(False)

#changing interaction mode based on data extents
renderView3.CameraPosition = [7.5, 6.5, 10000.0]
renderView3.CameraFocalPoint = [7.5, 6.5, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
fndn_axi_NAMC_v1_3_MeshData_00Display.SetScalarBarVisibility(renderView3, True)

# show data in view
fndn_axi_NAMC_v1_3_MPScalar_00Display = Show(fndn_axi_NAMC_v1_3_MPScalar_00, renderView3, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'pressure_liquid'
pressure_liquidLUT = GetColorTransferFunction('pressure_liquid')

# get opacity transfer function/opacity map for 'pressure_liquid'
pressure_liquidPWF = GetOpacityTransferFunction('pressure_liquid')

# trace defaults for the display properties.
fndn_axi_NAMC_v1_3_MPScalar_00Display.Selection = None
fndn_axi_NAMC_v1_3_MPScalar_00Display.Representation = 'Surface'
fndn_axi_NAMC_v1_3_MPScalar_00Display.ColorArrayName = ['POINTS', 'pressure_liquid']
fndn_axi_NAMC_v1_3_MPScalar_00Display.LookupTable = pressure_liquidLUT
fndn_axi_NAMC_v1_3_MPScalar_00Display.MapScalars = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.MultiComponentsMapping = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.InterpolateScalarsBeforeMapping = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.Opacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PointSize = 2.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.LineWidth = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.RenderLinesAsTubes = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.RenderPointsAsSpheres = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.Interpolation = 'Gouraud'
fndn_axi_NAMC_v1_3_MPScalar_00Display.Specular = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SpecularColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.SpecularPower = 100.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.Luminosity = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.Ambient = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.Diffuse = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.Roughness = 0.3
fndn_axi_NAMC_v1_3_MPScalar_00Display.Metallic = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.EdgeTint = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.Anisotropy = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.AnisotropyRotation = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.BaseIOR = 1.5
fndn_axi_NAMC_v1_3_MPScalar_00Display.CoatStrength = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.CoatIOR = 2.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.CoatRoughness = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.CoatColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectTCoordArray = 'None'
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectNormalArray = 'None'
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectTangentArray = 'None'
fndn_axi_NAMC_v1_3_MPScalar_00Display.Texture = None
fndn_axi_NAMC_v1_3_MPScalar_00Display.RepeatTextures = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.InterpolateTextures = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SeamlessU = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SeamlessV = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.UseMipmapTextures = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.ShowTexturesOnBackface = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.BaseColorTexture = None
fndn_axi_NAMC_v1_3_MPScalar_00Display.NormalTexture = None
fndn_axi_NAMC_v1_3_MPScalar_00Display.NormalScale = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.CoatNormalTexture = None
fndn_axi_NAMC_v1_3_MPScalar_00Display.CoatNormalScale = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.MaterialTexture = None
fndn_axi_NAMC_v1_3_MPScalar_00Display.OcclusionStrength = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.AnisotropyTexture = None
fndn_axi_NAMC_v1_3_MPScalar_00Display.EmissiveTexture = None
fndn_axi_NAMC_v1_3_MPScalar_00Display.EmissiveFactor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.FlipTextures = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.BackfaceRepresentation = 'Follow Frontface'
fndn_axi_NAMC_v1_3_MPScalar_00Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.BackfaceOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.Position = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.Scale = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.Orientation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.Origin = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
fndn_axi_NAMC_v1_3_MPScalar_00Display.Pickable = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.Triangulate = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.UseShaderReplacements = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.ShaderReplacements = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.NonlinearSubdivisionLevel = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.UseDataPartitions = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.OSPRayUseScaleArray = 'All Approximate'
fndn_axi_NAMC_v1_3_MPScalar_00Display.OSPRayScaleArray = 'pressure_liquid'
fndn_axi_NAMC_v1_3_MPScalar_00Display.OSPRayScaleFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MPScalar_00Display.OSPRayMaterial = 'None'
fndn_axi_NAMC_v1_3_MPScalar_00Display.BlockSelectors = ['/']
fndn_axi_NAMC_v1_3_MPScalar_00Display.BlockColors = []
fndn_axi_NAMC_v1_3_MPScalar_00Display.BlockOpacities = []
fndn_axi_NAMC_v1_3_MPScalar_00Display.Orient = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.OrientationMode = 'Direction'
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectOrientationVectors = 'None'
fndn_axi_NAMC_v1_3_MPScalar_00Display.Scaling = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.ScaleMode = 'No Data Scaling Off'
fndn_axi_NAMC_v1_3_MPScalar_00Display.ScaleFactor = 1.4844497883017966
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectScaleArray = 'pressure_liquid'
fndn_axi_NAMC_v1_3_MPScalar_00Display.GlyphType = 'Arrow'
fndn_axi_NAMC_v1_3_MPScalar_00Display.UseGlyphTable = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.GlyphTableIndexArray = 'pressure_liquid'
fndn_axi_NAMC_v1_3_MPScalar_00Display.UseCompositeGlyphTable = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.UseGlyphCullingAndLOD = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.LODValues = []
fndn_axi_NAMC_v1_3_MPScalar_00Display.ColorByLODIndex = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.GaussianRadius = 0.07422248941508983
fndn_axi_NAMC_v1_3_MPScalar_00Display.ShaderPreset = 'Sphere'
fndn_axi_NAMC_v1_3_MPScalar_00Display.CustomTriangleScale = 3
fndn_axi_NAMC_v1_3_MPScalar_00Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
fndn_axi_NAMC_v1_3_MPScalar_00Display.Emissive = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.ScaleByArray = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SetScaleArray = ['POINTS', 'pressure_liquid']
fndn_axi_NAMC_v1_3_MPScalar_00Display.ScaleArrayComponent = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.UseScaleFunction = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.ScaleTransferFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MPScalar_00Display.OpacityByArray = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.OpacityArray = ['POINTS', 'pressure_liquid']
fndn_axi_NAMC_v1_3_MPScalar_00Display.OpacityArrayComponent = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.OpacityTransferFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid = 'GridAxesRepresentation'
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionCellLabelBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionCellLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionCellLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionCellLabelFontSize = 18
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionCellLabelItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionCellLabelJustification = 'Left'
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionCellLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionCellLabelShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionPointLabelBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionPointLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionPointLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionPointLabelFontSize = 18
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionPointLabelItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionPointLabelJustification = 'Left'
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionPointLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectionPointLabelShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes = 'PolarAxesRepresentation'
fndn_axi_NAMC_v1_3_MPScalar_00Display.ScalarOpacityFunction = pressure_liquidPWF
fndn_axi_NAMC_v1_3_MPScalar_00Display.ScalarOpacityUnitDistance = 1.1582122559990673
fndn_axi_NAMC_v1_3_MPScalar_00Display.UseSeparateOpacityArray = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.OpacityArrayName = ['POINTS', 'pressure_liquid']
fndn_axi_NAMC_v1_3_MPScalar_00Display.OpacityComponent = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.SelectMapper = 'Projected tetra'
fndn_axi_NAMC_v1_3_MPScalar_00Display.SamplingDimensions = [128, 128, 128]
fndn_axi_NAMC_v1_3_MPScalar_00Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fndn_axi_NAMC_v1_3_MPScalar_00Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
fndn_axi_NAMC_v1_3_MPScalar_00Display.GlyphType.TipResolution = 6
fndn_axi_NAMC_v1_3_MPScalar_00Display.GlyphType.TipRadius = 0.1
fndn_axi_NAMC_v1_3_MPScalar_00Display.GlyphType.TipLength = 0.35
fndn_axi_NAMC_v1_3_MPScalar_00Display.GlyphType.ShaftResolution = 6
fndn_axi_NAMC_v1_3_MPScalar_00Display.GlyphType.ShaftRadius = 0.03
fndn_axi_NAMC_v1_3_MPScalar_00Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fndn_axi_NAMC_v1_3_MPScalar_00Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fndn_axi_NAMC_v1_3_MPScalar_00Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XTitle = 'X Axis'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YTitle = 'Y Axis'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZTitle = 'Z Axis'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XTitleBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XTitleItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XTitleShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YTitleBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YTitleItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YTitleShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZTitleBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZTitleItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZTitleShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.FacesToRender = 63
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.CullBackface = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.CullFrontface = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ShowGrid = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ShowEdges = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ShowTicks = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.AxesToLabel = 63
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XLabelBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XLabelItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XLabelShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YLabelBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YLabelItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YLabelShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZLabelBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZLabelItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZLabelShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XAxisPrecision = 2
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.XAxisLabels = []
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YAxisPrecision = 2
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.YAxisLabels = []
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZAxisPrecision = 2
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.ZAxisLabels = []
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.UseCustomBounds = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.Visibility = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.EnableCustomRange = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.CustomRange = [0.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.RadialAxesVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.DrawRadialGridlines = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarArcsVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.DrawPolarArcsGridlines = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.NumberOfRadialAxes = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.AutoSubdividePolarAxis = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.NumberOfPolarAxis = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.MinimumRadius = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.MinimumAngle = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.MaximumAngle = 90.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.Ratio = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitleVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarLabelVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.RadialLabelVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.RadialLabelLocation = 'Bottom'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.RadialUnitsVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.ScreenSize = 10.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitleBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitleItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitleShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisLabelBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisLabelItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisLabelShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisTextFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisTextBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisTextItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisTextShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisTextFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SecondaryRadialAxesTextBold = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.EnableDistanceLOD = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.DistanceLODThreshold = 0.7
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.EnableViewAngleLOD = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.ViewAngleLODThreshold = 0.7
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarTicksVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.TickLocation = 'Both'
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.AxisTickVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.AxisMinorTickVisibility = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.ArcTickVisibility = 1
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.ArcMinorTickVisibility = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.DeltaAngleMajor = 10.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.DeltaAngleMinor = 5.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.ArcMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.ArcTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.ArcMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.ArcTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.Use2DMode = 0
fndn_axi_NAMC_v1_3_MPScalar_00Display.PolarAxes.UseLogAxis = 0

# show color bar/color legend
fndn_axi_NAMC_v1_3_MPScalar_00Display.SetScalarBarVisibility(renderView3, True)

# show data in view
fndn_axi_NAMC_v1_3_MPTensor_00Display = Show(fndn_axi_NAMC_v1_3_MPTensor_00, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
fndn_axi_NAMC_v1_3_MPTensor_00Display.Selection = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.Representation = 'Surface'
fndn_axi_NAMC_v1_3_MPTensor_00Display.ColorArrayName = [None, '']
fndn_axi_NAMC_v1_3_MPTensor_00Display.LookupTable = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.MapScalars = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.MultiComponentsMapping = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.InterpolateScalarsBeforeMapping = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.Opacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PointSize = 2.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.LineWidth = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.RenderLinesAsTubes = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.RenderPointsAsSpheres = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.Interpolation = 'Gouraud'
fndn_axi_NAMC_v1_3_MPTensor_00Display.Specular = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SpecularColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.SpecularPower = 100.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.Luminosity = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.Ambient = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.Diffuse = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.Roughness = 0.3
fndn_axi_NAMC_v1_3_MPTensor_00Display.Metallic = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.EdgeTint = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.Anisotropy = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.AnisotropyRotation = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.BaseIOR = 1.5
fndn_axi_NAMC_v1_3_MPTensor_00Display.CoatStrength = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.CoatIOR = 2.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.CoatRoughness = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.CoatColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectTCoordArray = 'None'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectNormalArray = 'None'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectTangentArray = 'None'
fndn_axi_NAMC_v1_3_MPTensor_00Display.Texture = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.RepeatTextures = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.InterpolateTextures = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SeamlessU = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SeamlessV = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.UseMipmapTextures = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.ShowTexturesOnBackface = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.BaseColorTexture = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.NormalTexture = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.NormalScale = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.CoatNormalTexture = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.CoatNormalScale = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.MaterialTexture = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.OcclusionStrength = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.AnisotropyTexture = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.EmissiveTexture = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.EmissiveFactor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.FlipTextures = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.BackfaceRepresentation = 'Follow Frontface'
fndn_axi_NAMC_v1_3_MPTensor_00Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.BackfaceOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.Position = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.Scale = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.Orientation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.Origin = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
fndn_axi_NAMC_v1_3_MPTensor_00Display.Pickable = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.Triangulate = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.UseShaderReplacements = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.ShaderReplacements = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.NonlinearSubdivisionLevel = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.UseDataPartitions = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.OSPRayUseScaleArray = 'All Approximate'
fndn_axi_NAMC_v1_3_MPTensor_00Display.OSPRayScaleArray = 'eff_stress_solid'
fndn_axi_NAMC_v1_3_MPTensor_00Display.OSPRayScaleFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MPTensor_00Display.OSPRayMaterial = 'None'
fndn_axi_NAMC_v1_3_MPTensor_00Display.BlockSelectors = ['/']
fndn_axi_NAMC_v1_3_MPTensor_00Display.BlockColors = []
fndn_axi_NAMC_v1_3_MPTensor_00Display.BlockOpacities = []
fndn_axi_NAMC_v1_3_MPTensor_00Display.Orient = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.OrientationMode = 'Direction'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectOrientationVectors = 'None'
fndn_axi_NAMC_v1_3_MPTensor_00Display.Scaling = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.ScaleMode = 'No Data Scaling Off'
fndn_axi_NAMC_v1_3_MPTensor_00Display.ScaleFactor = 1.4844497883017966
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectScaleArray = 'None'
fndn_axi_NAMC_v1_3_MPTensor_00Display.GlyphType = 'Arrow'
fndn_axi_NAMC_v1_3_MPTensor_00Display.UseGlyphTable = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.GlyphTableIndexArray = 'None'
fndn_axi_NAMC_v1_3_MPTensor_00Display.UseCompositeGlyphTable = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.UseGlyphCullingAndLOD = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.LODValues = []
fndn_axi_NAMC_v1_3_MPTensor_00Display.ColorByLODIndex = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.GaussianRadius = 0.07422248941508983
fndn_axi_NAMC_v1_3_MPTensor_00Display.ShaderPreset = 'Sphere'
fndn_axi_NAMC_v1_3_MPTensor_00Display.CustomTriangleScale = 3
fndn_axi_NAMC_v1_3_MPTensor_00Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
fndn_axi_NAMC_v1_3_MPTensor_00Display.Emissive = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.ScaleByArray = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SetScaleArray = ['POINTS', 'eff_stress_solid']
fndn_axi_NAMC_v1_3_MPTensor_00Display.ScaleArrayComponent = '0'
fndn_axi_NAMC_v1_3_MPTensor_00Display.UseScaleFunction = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.ScaleTransferFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MPTensor_00Display.OpacityByArray = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.OpacityArray = ['POINTS', 'eff_stress_solid']
fndn_axi_NAMC_v1_3_MPTensor_00Display.OpacityArrayComponent = '0'
fndn_axi_NAMC_v1_3_MPTensor_00Display.OpacityTransferFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid = 'GridAxesRepresentation'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionCellLabelBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionCellLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionCellLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionCellLabelFontSize = 18
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionCellLabelItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionCellLabelJustification = 'Left'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionCellLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionCellLabelShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionPointLabelBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionPointLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionPointLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionPointLabelFontSize = 18
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionPointLabelItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionPointLabelJustification = 'Left'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionPointLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectionPointLabelShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes = 'PolarAxesRepresentation'
fndn_axi_NAMC_v1_3_MPTensor_00Display.ScalarOpacityFunction = None
fndn_axi_NAMC_v1_3_MPTensor_00Display.ScalarOpacityUnitDistance = 1.1582122559990673
fndn_axi_NAMC_v1_3_MPTensor_00Display.UseSeparateOpacityArray = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.OpacityArrayName = ['POINTS', 'eff_stress_solid']
fndn_axi_NAMC_v1_3_MPTensor_00Display.OpacityComponent = '0'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SelectMapper = 'Projected tetra'
fndn_axi_NAMC_v1_3_MPTensor_00Display.SamplingDimensions = [128, 128, 128]
fndn_axi_NAMC_v1_3_MPTensor_00Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fndn_axi_NAMC_v1_3_MPTensor_00Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
fndn_axi_NAMC_v1_3_MPTensor_00Display.GlyphType.TipResolution = 6
fndn_axi_NAMC_v1_3_MPTensor_00Display.GlyphType.TipRadius = 0.1
fndn_axi_NAMC_v1_3_MPTensor_00Display.GlyphType.TipLength = 0.35
fndn_axi_NAMC_v1_3_MPTensor_00Display.GlyphType.ShaftResolution = 6
fndn_axi_NAMC_v1_3_MPTensor_00Display.GlyphType.ShaftRadius = 0.03
fndn_axi_NAMC_v1_3_MPTensor_00Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fndn_axi_NAMC_v1_3_MPTensor_00Display.ScaleTransferFunction.Points = [-42.29847187500009, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fndn_axi_NAMC_v1_3_MPTensor_00Display.OpacityTransferFunction.Points = [-42.29847187500009, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XTitle = 'X Axis'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YTitle = 'Y Axis'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZTitle = 'Z Axis'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XTitleBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XTitleItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XTitleShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YTitleBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YTitleItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YTitleShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZTitleBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZTitleItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZTitleShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.FacesToRender = 63
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.CullBackface = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.CullFrontface = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ShowGrid = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ShowEdges = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ShowTicks = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.AxesToLabel = 63
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XLabelBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XLabelItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XLabelShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YLabelBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YLabelItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YLabelShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZLabelBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZLabelItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZLabelShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XAxisPrecision = 2
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.XAxisLabels = []
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YAxisPrecision = 2
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.YAxisLabels = []
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZAxisPrecision = 2
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.ZAxisLabels = []
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.UseCustomBounds = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.Visibility = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.EnableCustomRange = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.CustomRange = [0.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.RadialAxesVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.DrawRadialGridlines = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarArcsVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.DrawPolarArcsGridlines = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.NumberOfRadialAxes = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.AutoSubdividePolarAxis = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.NumberOfPolarAxis = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.MinimumRadius = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.MinimumAngle = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.MaximumAngle = 90.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.Ratio = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitleVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarLabelVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.RadialLabelVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.RadialLabelLocation = 'Bottom'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.RadialUnitsVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.ScreenSize = 10.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitleBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitleItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitleShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisLabelBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisLabelItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisLabelShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisTextFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisTextBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisTextItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisTextShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisTextFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SecondaryRadialAxesTextBold = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.EnableDistanceLOD = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.DistanceLODThreshold = 0.7
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.EnableViewAngleLOD = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.ViewAngleLODThreshold = 0.7
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarTicksVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.TickLocation = 'Both'
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.AxisTickVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.AxisMinorTickVisibility = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.ArcTickVisibility = 1
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.ArcMinorTickVisibility = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.DeltaAngleMajor = 10.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.DeltaAngleMinor = 5.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.ArcMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.ArcTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.ArcMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.ArcTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.Use2DMode = 0
fndn_axi_NAMC_v1_3_MPTensor_00Display.PolarAxes.UseLogAxis = 0

# show data in view
fndn_axi_NAMC_v1_3_MPVector_00Display = Show(fndn_axi_NAMC_v1_3_MPVector_00, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
fndn_axi_NAMC_v1_3_MPVector_00Display.Selection = None
fndn_axi_NAMC_v1_3_MPVector_00Display.Representation = 'Surface'
fndn_axi_NAMC_v1_3_MPVector_00Display.ColorArrayName = [None, '']
fndn_axi_NAMC_v1_3_MPVector_00Display.LookupTable = None
fndn_axi_NAMC_v1_3_MPVector_00Display.MapScalars = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.MultiComponentsMapping = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.InterpolateScalarsBeforeMapping = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.Opacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PointSize = 2.0
fndn_axi_NAMC_v1_3_MPVector_00Display.LineWidth = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.RenderLinesAsTubes = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.RenderPointsAsSpheres = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.Interpolation = 'Gouraud'
fndn_axi_NAMC_v1_3_MPVector_00Display.Specular = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.SpecularColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.SpecularPower = 100.0
fndn_axi_NAMC_v1_3_MPVector_00Display.Luminosity = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.Ambient = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.Diffuse = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.Roughness = 0.3
fndn_axi_NAMC_v1_3_MPVector_00Display.Metallic = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.EdgeTint = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.Anisotropy = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.AnisotropyRotation = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.BaseIOR = 1.5
fndn_axi_NAMC_v1_3_MPVector_00Display.CoatStrength = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.CoatIOR = 2.0
fndn_axi_NAMC_v1_3_MPVector_00Display.CoatRoughness = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.CoatColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectTCoordArray = 'None'
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectNormalArray = 'None'
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectTangentArray = 'None'
fndn_axi_NAMC_v1_3_MPVector_00Display.Texture = None
fndn_axi_NAMC_v1_3_MPVector_00Display.RepeatTextures = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.InterpolateTextures = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.SeamlessU = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.SeamlessV = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.UseMipmapTextures = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.ShowTexturesOnBackface = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.BaseColorTexture = None
fndn_axi_NAMC_v1_3_MPVector_00Display.NormalTexture = None
fndn_axi_NAMC_v1_3_MPVector_00Display.NormalScale = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.CoatNormalTexture = None
fndn_axi_NAMC_v1_3_MPVector_00Display.CoatNormalScale = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.MaterialTexture = None
fndn_axi_NAMC_v1_3_MPVector_00Display.OcclusionStrength = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.AnisotropyTexture = None
fndn_axi_NAMC_v1_3_MPVector_00Display.EmissiveTexture = None
fndn_axi_NAMC_v1_3_MPVector_00Display.EmissiveFactor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.FlipTextures = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.BackfaceRepresentation = 'Follow Frontface'
fndn_axi_NAMC_v1_3_MPVector_00Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.BackfaceOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.Position = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.Scale = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.Orientation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.Origin = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
fndn_axi_NAMC_v1_3_MPVector_00Display.Pickable = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.Triangulate = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.UseShaderReplacements = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.ShaderReplacements = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.NonlinearSubdivisionLevel = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.UseDataPartitions = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.OSPRayUseScaleArray = 'All Approximate'
fndn_axi_NAMC_v1_3_MPVector_00Display.OSPRayScaleArray = 'acceleration_solid'
fndn_axi_NAMC_v1_3_MPVector_00Display.OSPRayScaleFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MPVector_00Display.OSPRayMaterial = 'None'
fndn_axi_NAMC_v1_3_MPVector_00Display.BlockSelectors = ['/']
fndn_axi_NAMC_v1_3_MPVector_00Display.BlockColors = []
fndn_axi_NAMC_v1_3_MPVector_00Display.BlockOpacities = []
fndn_axi_NAMC_v1_3_MPVector_00Display.Orient = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.OrientationMode = 'Direction'
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectOrientationVectors = 'velocity_solid'
fndn_axi_NAMC_v1_3_MPVector_00Display.Scaling = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.ScaleMode = 'No Data Scaling Off'
fndn_axi_NAMC_v1_3_MPVector_00Display.ScaleFactor = 1.4844497883017966
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectScaleArray = 'None'
fndn_axi_NAMC_v1_3_MPVector_00Display.GlyphType = 'Arrow'
fndn_axi_NAMC_v1_3_MPVector_00Display.UseGlyphTable = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.GlyphTableIndexArray = 'None'
fndn_axi_NAMC_v1_3_MPVector_00Display.UseCompositeGlyphTable = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.UseGlyphCullingAndLOD = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.LODValues = []
fndn_axi_NAMC_v1_3_MPVector_00Display.ColorByLODIndex = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.GaussianRadius = 0.07422248941508983
fndn_axi_NAMC_v1_3_MPVector_00Display.ShaderPreset = 'Sphere'
fndn_axi_NAMC_v1_3_MPVector_00Display.CustomTriangleScale = 3
fndn_axi_NAMC_v1_3_MPVector_00Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
fndn_axi_NAMC_v1_3_MPVector_00Display.Emissive = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.ScaleByArray = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.SetScaleArray = ['POINTS', 'acceleration_solid']
fndn_axi_NAMC_v1_3_MPVector_00Display.ScaleArrayComponent = 'X'
fndn_axi_NAMC_v1_3_MPVector_00Display.UseScaleFunction = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.ScaleTransferFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MPVector_00Display.OpacityByArray = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.OpacityArray = ['POINTS', 'acceleration_solid']
fndn_axi_NAMC_v1_3_MPVector_00Display.OpacityArrayComponent = 'X'
fndn_axi_NAMC_v1_3_MPVector_00Display.OpacityTransferFunction = 'PiecewiseFunction'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid = 'GridAxesRepresentation'
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionCellLabelBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionCellLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionCellLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionCellLabelFontSize = 18
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionCellLabelItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionCellLabelJustification = 'Left'
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionCellLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionCellLabelShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionPointLabelBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionPointLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionPointLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionPointLabelFontSize = 18
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionPointLabelItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionPointLabelJustification = 'Left'
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionPointLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectionPointLabelShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes = 'PolarAxesRepresentation'
fndn_axi_NAMC_v1_3_MPVector_00Display.ScalarOpacityFunction = None
fndn_axi_NAMC_v1_3_MPVector_00Display.ScalarOpacityUnitDistance = 1.1582122559990673
fndn_axi_NAMC_v1_3_MPVector_00Display.UseSeparateOpacityArray = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.OpacityArrayName = ['POINTS', 'acceleration_solid']
fndn_axi_NAMC_v1_3_MPVector_00Display.OpacityComponent = 'X'
fndn_axi_NAMC_v1_3_MPVector_00Display.SelectMapper = 'Projected tetra'
fndn_axi_NAMC_v1_3_MPVector_00Display.SamplingDimensions = [128, 128, 128]
fndn_axi_NAMC_v1_3_MPVector_00Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fndn_axi_NAMC_v1_3_MPVector_00Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
fndn_axi_NAMC_v1_3_MPVector_00Display.GlyphType.TipResolution = 6
fndn_axi_NAMC_v1_3_MPVector_00Display.GlyphType.TipRadius = 0.1
fndn_axi_NAMC_v1_3_MPVector_00Display.GlyphType.TipLength = 0.35
fndn_axi_NAMC_v1_3_MPVector_00Display.GlyphType.ShaftResolution = 6
fndn_axi_NAMC_v1_3_MPVector_00Display.GlyphType.ShaftRadius = 0.03
fndn_axi_NAMC_v1_3_MPVector_00Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fndn_axi_NAMC_v1_3_MPVector_00Display.ScaleTransferFunction.Points = [-0.03620532546754321, 0.0, 0.5, 0.0, 0.06923996524564695, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fndn_axi_NAMC_v1_3_MPVector_00Display.OpacityTransferFunction.Points = [-0.03620532546754321, 0.0, 0.5, 0.0, 0.06923996524564695, 1.0, 0.5, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XTitle = 'X Axis'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YTitle = 'Y Axis'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZTitle = 'Z Axis'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XTitleBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XTitleItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XTitleShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YTitleBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YTitleItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YTitleShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZTitleBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZTitleItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZTitleShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.FacesToRender = 63
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.CullBackface = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.CullFrontface = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ShowGrid = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ShowEdges = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ShowTicks = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.AxesToLabel = 63
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XLabelBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XLabelItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XLabelShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YLabelBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YLabelItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YLabelShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZLabelBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZLabelItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZLabelShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XAxisPrecision = 2
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.XAxisLabels = []
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YAxisPrecision = 2
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.YAxisLabels = []
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZAxisNotation = 'Mixed'
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZAxisPrecision = 2
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZAxisUseCustomLabels = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.ZAxisLabels = []
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.UseCustomBounds = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.Visibility = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.EnableCustomRange = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.CustomRange = [0.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.RadialAxesVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.DrawRadialGridlines = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarArcsVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.DrawPolarArcsGridlines = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.NumberOfRadialAxes = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.AutoSubdividePolarAxis = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.NumberOfPolarAxis = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.MinimumRadius = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.MinimumAngle = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.MaximumAngle = 90.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.Ratio = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitleVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarLabelVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.RadialLabelVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.RadialLabelLocation = 'Bottom'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.RadialUnitsVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.ScreenSize = 10.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitleOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitleFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitleBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitleItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitleShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTitleFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisLabelOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisLabelFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisLabelBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisLabelItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisLabelShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisLabelFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisTextFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisTextBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisTextItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisTextShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisTextFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SecondaryRadialAxesTextBold = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.EnableDistanceLOD = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.DistanceLODThreshold = 0.7
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.EnableViewAngleLOD = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.ViewAngleLODThreshold = 0.7
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarTicksVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.TickLocation = 'Both'
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.AxisTickVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.AxisMinorTickVisibility = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.ArcTickVisibility = 1
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.ArcMinorTickVisibility = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.DeltaAngleMajor = 10.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.DeltaAngleMinor = 5.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.ArcMajorTickSize = 0.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.ArcTickRatioSize = 0.3
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.ArcMajorTickThickness = 1.0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.ArcTickRatioThickness = 0.5
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.Use2DMode = 0
fndn_axi_NAMC_v1_3_MPVector_00Display.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView3.Update()

# hide data in view
Hide(fndn_axi_NAMC_v1_3_MPTensor_00, renderView3)

# hide data in view
Hide(fndn_axi_NAMC_v1_3_MPVector_00, renderView3)

# set active source
SetActiveSource(fndn_axi_NAMC_v1_3_MeshData_00)

# change representation type
fndn_axi_NAMC_v1_3_MeshData_00Display.SetRepresentationType('Wireframe')

# set active source
SetActiveSource(fndn_axi_NAMC_v1_3_MPScalar_00)

# set scalar coloring
ColorBy(fndn_axi_NAMC_v1_3_MPScalar_00Display, ('POINTS', 'deviatoric_strain_solid'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pressure_liquidLUT, renderView3)

# rescale color and/or opacity maps used to include current data range
fndn_axi_NAMC_v1_3_MPScalar_00Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
fndn_axi_NAMC_v1_3_MPScalar_00Display.SetScalarBarVisibility(renderView3, True)

# get color transfer function/color map for 'deviatoric_strain_solid'
deviatoric_strain_solidLUT = GetColorTransferFunction('deviatoric_strain_solid')

# get opacity transfer function/opacity map for 'deviatoric_strain_solid'
deviatoric_strain_solidPWF = GetOpacityTransferFunction('deviatoric_strain_solid')

# change representation type
fndn_axi_NAMC_v1_3_MPScalar_00Display.SetRepresentationType('Points')

# Properties modified on fndn_axi_NAMC_v1_3_MPScalar_00Display
fndn_axi_NAMC_v1_3_MPScalar_00Display.PointSize = 5.0

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1369, 816)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView3
renderView3.InteractionMode = '2D'
renderView3.CameraPosition = [7.5, 6.5, 10000.0]
renderView3.CameraFocalPoint = [7.5, 6.5, 0.0]
renderView3.CameraParallelScale = 9.924716620639604

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).