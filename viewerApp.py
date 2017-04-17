from vtk import* 


# create camera
camera =vtkCamera ();
camera.SetPosition(0, 0,100);
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

#render, start
renderWindow.Render();
