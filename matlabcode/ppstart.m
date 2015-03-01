function H = ppstart

% PPSTART is a function m-file that is read when PPLANE5 
%         is started and which inputs certain data that 
%         are used to change defaults.  Only three items 
%         allowed.  If only one item is to be changed, all 
%         three should be included.  The following are the 
%         defaults as written in PPLANE5, and changes can 
%         be made as needed.

H =[];     % DO NOT REMOVE THIS LINE!
           % This command is essential to the working of this function.  It
           % is necessary if this file exists, even if no changes follow it.
	   
H.style = 'display';	% Choices are 'white','black', or 'display', 
                        % The default is 'white'.

H.size = 18;	     % Any number is allowed.  This is the 
                     % main font size used in PPLANE5.  It 
                     % determines the size of all windows,
                     % and everything else.  The default is 10.

% H.ppdir = 'e:\matlab';		% The directory where systems and 
                  % galleries are to be found.  This must be 
                  % a string like:
                  %    'c:\Matlab\files'   (PC)
                  %    '/home/polking/matlab/files'  (UNIX)
                  %    'Macintosh HD:Matlab:files'   (Mac)                  

% H.npts = 15;   % The number of field points per line.  The default is 20.

% H.solver = 'Runge-Kutta 4';  % The choices are 'Dormand Prince', 'ode15s',
                              % and 'Runge-Kutta 4'.  The default is 
			      % 'Dormand Prince'.
			      
% H.tolerance = 1e-5;  % The tolerance used by the Dormand Prince and ode15s
                     % solvers.  It should be at most 1e-3 and at least
                     % 1e-12.  The default is 5e-4.
		     
% H.stepsize = 0.01;   % The step size used by the Runge-Kutta 4 solver.
                     % The default is 0.1;
