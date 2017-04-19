from vtk import* 


reader = vtkOBJReader();
path = "./vanquish.obj";
reader.SetFileName(path);
reader.Update();

#Create a sphere
sphereSource =vtkSphereSource();
sphereSource.SetCenter(0.0, 0.0, 0.0);
sphereSource.SetRadius(1);
sphereSource.Update();
 
mapper = vtkPolyDataMapper();
mapper.SetInputConnection(reader.GetOutputPort());
 
mapper2 = vtkPolyDataMapper();
mapper2.SetInputConnection(sphereSource.GetOutputPort());


actor = vtkActor();
actor.SetMapper(mapper);

actor2 = vtkActor();
actor2.SetMapper(mapper2);


# create camera
camera =vtkCamera ();
camera.SetPosition(0, 0,4);
camera.SetFocalPoint(0, 0, 0);

# from lab 1, camera.py
# Create a renderer, render window, and interactor
renderer =vtkRenderer();
renderer.SetActiveCamera(camera);
 
renderWindow =vtkRenderWindow();
renderWindow.AddRenderer(renderer);
renderWindowInteractor =vtkRenderWindowInteractor();
renderWindowInteractor.SetRenderWindow(renderWindow);

renderer.SetBackground(1,1,1); # Background color white
renderer.AddActor(actor);
renderer.AddActor(actor2);

#render, start
renderWindow.Render();
renderWindowInteractor.Start();
