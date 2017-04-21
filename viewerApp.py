from vtk import* 

# create camera
camera =vtkCamera ();
camera.SetPosition(0, 0, 4);
camera.SetFocalPoint(0, 0, 0);

# Create a renderer, render window, and interactor
renderer =vtkRenderer();
renderer.SetActiveCamera(camera);
 
renderWindow =vtkRenderWindow();
renderWindow.AddRenderer(renderer);

renderWindowInteractor =vtkRenderWindowInteractor();
renderWindowInteractor.SetRenderWindow(renderWindow);

renderer.SetBackground(1,1,1); # Background



# # Read in Iron Man
# reader = vtkOBJReader();
# filename = "./ironman.obj";
# reader.SetFileName(filename);
# reader.Update();

# # put obj file data to mapper
# objFile = vtkPolyDataMapper();
# objFile.SetInputConnection(reader.GetOutputPort());

# # put mapper into an actor
# objActor = vtkActor();
# objActor1.SetPosition(10,0.0,0.0);
# objActor.SetMapper(objFile);


# # render the obj Actor
# renderer.AddActor(objActor);

# ******************************** Read obj file 
reader1 = vtkOBJReader();
filename = "./vanquish.obj";
reader1.SetFileName(filename);
reader1.Update();

# put obj file data to mapper
objFile1 = vtkPolyDataMapper();
objFile1.SetInputConnection(reader1.GetOutputPort());

# put mapper into an actor
objActor1 = vtkActor();
objActor1.SetPosition(0.0,0.9,0.0);
objActor1.GetProperty().SetColor(255,255, 255);
objActor1.SetMapper(objFile1);

# render the obj Actor
renderer.AddActor(objActor1);



# ******************************* Create a sphere
sphereSource =vtkSphereSource();
sphereSource.SetCenter(0.0, 0.0, 0.0);
sphereSource.SetRadius(1);
sphereSource.Update();

# throw data into mapper
sphere_mapper = vtkPolyDataMapper();
sphere_mapper.SetInputConnection(sphereSource.GetOutputPort());

# create actor from mappers
sphere_actor = vtkActor();
sphere_actor.SetMapper(sphere_mapper);

# render the Sphere Actor
renderer.AddActor(sphere_actor);



#******************************  Add the axes
axes = vtkAxesActor();
axes.SetTotalLength(2,2,2);

transform = vtkTransform();
transform.Translate(2.0, 0.0, 0.0);
axes.SetUserTransform(transform);

renderer.AddActor(axes);

light = vtkLight();
light.SetColor(1.0, 0.0, 0.0);
renderer.AddLight(light);



# Render and start
renderWindow.Render();
renderWindowInteractor.Start();
