classdef quad_eq_exported < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        UIFigure                     matlab.ui.Figure
        Image                        matlab.ui.control.Image
        increasexareaifyouneedLabel  matlab.ui.control.Label
        AnswersLabel                 matlab.ui.control.Label
        TypeparametersLabel          matlab.ui.control.Label
        RedThemeCheckBox             matlab.ui.control.CheckBox
        x2EditField                  matlab.ui.control.NumericEditField
        x2EditFieldLabel             matlab.ui.control.Label
        x1EditField                  matlab.ui.control.NumericEditField
        x1EditFieldLabel             matlab.ui.control.Label
        NongridButtonGroup           matlab.ui.container.ButtonGroup
        rButton_3                    matlab.ui.control.RadioButton
        rButton_2                    matlab.ui.control.RadioButton
        rButton                      matlab.ui.control.RadioButton
        xradiusEditField             matlab.ui.control.NumericEditField
        xradiusEditFieldLabel        matlab.ui.control.Label
        SOLVEButton                  matlab.ui.control.Button
        ccoeffEditField              matlab.ui.control.NumericEditField
        ccoeffEditFieldLabel         matlab.ui.control.Label
        bcoeffEditField              matlab.ui.control.NumericEditField
        bcoeffEditFieldLabel         matlab.ui.control.Label
        acoeffEditField              matlab.ui.control.NumericEditField
        acoeffLabel                  matlab.ui.control.Label
        UIAxes                       matlab.ui.control.UIAxes
    end

    
    properties (Access = private)
        a = 1 % for acoeff
        b = 0 % for bcoeff
        c = 0 % for ccoeff
        r = 5 % for xradius
        N = 0 % for Nongrid
    end
    
    methods (Access = private)
        
    end
    

    % Callbacks that handle component events
    methods (Access = private)

        % Value changed function: acoeffEditField
        function acoeffEditFieldValueChanged(app, event)
            tmp = app.acoeffEditField.Value;
            if tmp ~= 0
                app.a = tmp;
            else
                app.acoeffEditField.Value = app.a;
            end
        end

        % Value changed function: bcoeffEditField
        function bcoeffEditFieldValueChanged(app, event)
            app.b = app.bcoeffEditField.Value;
        end

        % Value changed function: ccoeffEditField
        function ccoeffEditFieldValueChanged(app, event)
            app.c = app.ccoeffEditField.Value;
        end

        % Button pushed function: SOLVEButton
        function SOLVEButtonPushed(app, event)
            D = app.b ^ 2 - 4 * app.a * app.c;
            if D > 0
                app.x1EditField.Value = (- app.b + sqrt(D)) / (2 * app.a);
                app.x2EditField.Value = (- app.b - sqrt(D)) / (2 * app.a);
                app.x1EditField.Visible = true;
                app.x2EditField.Visible = true;
                plot(app.UIAxes, app.x1EditField.Value, 0, 'ro', app.x2EditField.Value, 0, 'ro')
                hold(app.UIAxes, 'on')
            elseif D == 0
                app.x1EditField.Value = - app.b / (2 * app.a);
                app.x2EditField.Value = - app.b / (2 * app.a);
                app.x1EditField.Visible = true;
                app.x2EditField.Visible = true;
                plot(app.UIAxes, app.x1EditField.Value, 0, 'ro')
                hold(app.UIAxes, 'on')
            elseif D < 0
                app.x1EditField.Visible = false;
                app.x2EditField.Visible = false;
            end
            
            if app.N == 0
                app.N = 4 * app.r;
            end
            x0 = - app.b / (2 * app.a);
            x = linspace((x0 - app.r), (x0 + app.r), app.N);
            zero_y = 0 * x;
            y = app.a * x .^ 2 + app.b * x + app.c;
            app.UIAxes.XLim = [min(x), max(x)];
            app.UIAxes.Interactions = [dataTipInteraction];
            plot(app.UIAxes, x, zero_y, 'r', x, y, 'black')
            app.UIAxes.XGrid = 'on';
            app.UIAxes.YGrid = 'on';
            hold(app.UIAxes, 'off');
        end

        % Value changed function: xradiusEditField
        function xradiusEditFieldValueChanged(app, event)
            app.r = app.xradiusEditField.Value;
        end

        % Selection changed function: NongridButtonGroup
        function NongridButtonGroupSelectionChanged(app, event)
            selectedButton = app.NongridButtonGroup.SelectedObject;
            if selectedButton == app.rButton
                app.N = app.r;
            elseif selectedButton == app.rButton_2
                app.N = 4 * app.r;
            elseif selectedButton == app.rButton_3
                app.N = 100 * app.r;
            end
        end

        % Value changed function: RedThemeCheckBox
        function RedThemeCheckBoxValueChanged(app, event)
            if app.RedThemeCheckBox.Value
               app.UIFigure.Color = [1.0, 0.7, 0.7];
            else
               app.UIFigure.Color = [0.94, 0.94, 0.94];
            end
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create UIFigure and hide until all components are created
            app.UIFigure = uifigure('Visible', 'off');
            app.UIFigure.Position = [100 100 640 480];
            app.UIFigure.Name = 'MATLAB App';

            % Create UIAxes
            app.UIAxes = uiaxes(app.UIFigure);
            xlabel(app.UIAxes, 'X')
            ylabel(app.UIAxes, 'Y')
            zlabel(app.UIAxes, 'Z')
            app.UIAxes.Position = [206 17 423 312];

            % Create acoeffLabel
            app.acoeffLabel = uilabel(app.UIFigure);
            app.acoeffLabel.HorizontalAlignment = 'right';
            app.acoeffLabel.Position = [25 395 41 22];
            app.acoeffLabel.Text = {'a coeff'; ''};

            % Create acoeffEditField
            app.acoeffEditField = uieditfield(app.UIFigure, 'numeric');
            app.acoeffEditField.ValueChangedFcn = createCallbackFcn(app, @acoeffEditFieldValueChanged, true);
            app.acoeffEditField.Position = [81 395 100 22];
            app.acoeffEditField.Value = 1;

            % Create bcoeffEditFieldLabel
            app.bcoeffEditFieldLabel = uilabel(app.UIFigure);
            app.bcoeffEditFieldLabel.HorizontalAlignment = 'right';
            app.bcoeffEditFieldLabel.Position = [25 352 41 22];
            app.bcoeffEditFieldLabel.Text = {'b coeff'; ''};

            % Create bcoeffEditField
            app.bcoeffEditField = uieditfield(app.UIFigure, 'numeric');
            app.bcoeffEditField.ValueChangedFcn = createCallbackFcn(app, @bcoeffEditFieldValueChanged, true);
            app.bcoeffEditField.Position = [81 352 100 22];

            % Create ccoeffEditFieldLabel
            app.ccoeffEditFieldLabel = uilabel(app.UIFigure);
            app.ccoeffEditFieldLabel.HorizontalAlignment = 'right';
            app.ccoeffEditFieldLabel.Position = [25 307 41 22];
            app.ccoeffEditFieldLabel.Text = {'c coeff'; ''};

            % Create ccoeffEditField
            app.ccoeffEditField = uieditfield(app.UIFigure, 'numeric');
            app.ccoeffEditField.ValueChangedFcn = createCallbackFcn(app, @ccoeffEditFieldValueChanged, true);
            app.ccoeffEditField.Position = [81 307 100 22];

            % Create SOLVEButton
            app.SOLVEButton = uibutton(app.UIFigure, 'push');
            app.SOLVEButton.ButtonPushedFcn = createCallbackFcn(app, @SOLVEButtonPushed, true);
            app.SOLVEButton.Position = [18 17 163 57];
            app.SOLVEButton.Text = 'SOLVE!';

            % Create xradiusEditFieldLabel
            app.xradiusEditFieldLabel = uilabel(app.UIFigure);
            app.xradiusEditFieldLabel.HorizontalAlignment = 'right';
            app.xradiusEditFieldLabel.Position = [18 260 48 22];
            app.xradiusEditFieldLabel.Text = {'x radius'; ''};

            % Create xradiusEditField
            app.xradiusEditField = uieditfield(app.UIFigure, 'numeric');
            app.xradiusEditField.ValueChangedFcn = createCallbackFcn(app, @xradiusEditFieldValueChanged, true);
            app.xradiusEditField.Position = [81 260 100 22];
            app.xradiusEditField.Value = 5;

            % Create NongridButtonGroup
            app.NongridButtonGroup = uibuttongroup(app.UIFigure);
            app.NongridButtonGroup.SelectionChangedFcn = createCallbackFcn(app, @NongridButtonGroupSelectionChanged, true);
            app.NongridButtonGroup.Title = 'N on grid';
            app.NongridButtonGroup.Position = [18 100 163 106];

            % Create rButton
            app.rButton = uiradiobutton(app.NongridButtonGroup);
            app.rButton.Text = 'r';
            app.rButton.Position = [11 60 58 22];

            % Create rButton_2
            app.rButton_2 = uiradiobutton(app.NongridButtonGroup);
            app.rButton_2.Text = '4r';
            app.rButton_2.Position = [11 38 65 22];
            app.rButton_2.Value = true;

            % Create rButton_3
            app.rButton_3 = uiradiobutton(app.NongridButtonGroup);
            app.rButton_3.Text = '100r';
            app.rButton_3.Position = [11 16 65 22];

            % Create x1EditFieldLabel
            app.x1EditFieldLabel = uilabel(app.UIFigure);
            app.x1EditFieldLabel.HorizontalAlignment = 'right';
            app.x1EditFieldLabel.Position = [216 395 25 22];
            app.x1EditFieldLabel.Text = 'x1';

            % Create x1EditField
            app.x1EditField = uieditfield(app.UIFigure, 'numeric');
            app.x1EditField.Editable = 'off';
            app.x1EditField.Visible = 'off';
            app.x1EditField.Position = [256 395 100 22];

            % Create x2EditFieldLabel
            app.x2EditFieldLabel = uilabel(app.UIFigure);
            app.x2EditFieldLabel.HorizontalAlignment = 'right';
            app.x2EditFieldLabel.Position = [216 352 25 22];
            app.x2EditFieldLabel.Text = 'x2';

            % Create x2EditField
            app.x2EditField = uieditfield(app.UIFigure, 'numeric');
            app.x2EditField.Editable = 'off';
            app.x2EditField.Visible = 'off';
            app.x2EditField.Position = [256 352 100 22];

            % Create RedThemeCheckBox
            app.RedThemeCheckBox = uicheckbox(app.UIFigure);
            app.RedThemeCheckBox.ValueChangedFcn = createCallbackFcn(app, @RedThemeCheckBoxValueChanged, true);
            app.RedThemeCheckBox.Text = 'Red Theme';
            app.RedThemeCheckBox.Position = [394 438 84 22];

            % Create TypeparametersLabel
            app.TypeparametersLabel = uilabel(app.UIFigure);
            app.TypeparametersLabel.Position = [18 438 152 22];
            app.TypeparametersLabel.Text = 'Type parameters:';

            % Create AnswersLabel
            app.AnswersLabel = uilabel(app.UIFigure);
            app.AnswersLabel.Position = [216 438 140 22];
            app.AnswersLabel.Text = 'Answers:';

            % Create increasexareaifyouneedLabel
            app.increasexareaifyouneedLabel = uilabel(app.UIFigure);
            app.increasexareaifyouneedLabel.Position = [18 230 168 22];
            app.increasexareaifyouneedLabel.Text = '(increase x area, if you need)';

            % Create Image
            app.Image = uiimage(app.UIFigure);
            app.Image.Position = [529 373 100 100];
            app.Image.ImageSource = 'cmc.png';

            % Show the figure after all components are created
            app.UIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = quad_eq_exported

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.UIFigure)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.UIFigure)
        end
    end
end