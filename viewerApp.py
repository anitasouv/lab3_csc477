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



# *****read obj file 
reader = vtkOBJReader();
filename = "./vanquish.obj";
reader.SetFileName(filename);
reader.Update();

# put obj file data to mapper
objFile = vtkPolyDataMapper();
objFile.SetInputConnection(reader.GetOutputPort());

# put mapper into an actor
objActor = vtkActor();
objActor.SetMapper(objFile);

# render the obj Actor
renderer.AddActor(objActor);



#*********Create a sphere
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




axes = vtkAxesActor();
axes.SetTotalLength(2,2,2);

renderer.AddActor(axes);



# Render and start
renderWindow.Render();
renderWindowInteractor.Start();
