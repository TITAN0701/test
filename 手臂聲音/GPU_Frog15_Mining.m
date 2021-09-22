clear all;
close all;
clc;

t0 = clock;                                         % �O���{�b���ɶ�


xlsFile = 'F15_MFCC_Simon.xlsx';
B = xlsread(xlsFile, 'F15_all', 'B1:B75');		    % Ū�X 'F15_all' Label���
C = xlsread(xlsFile, 'F15_all', 'C1:OL75');         % Ū�X 'F15_all' ���������
D = xlsread(xlsFile, 'F15_all_test', 'B1:OK15');    % ���� 'F15_all_test' �����n�����O�_���T

predict = zeros(15);                                % �w���ؼЭӼ�        15�ثC���n�����Ѻ���


% % SVM %
% svmModel=svmtrain (B, C);
% for i = 1:15
%      predict(i) = svmpredict(0,D(i,:),svmModel);
% end

% % SVM %
% % svmModel1=svmtrain(C,B,'kernel_function','linear','shoplot',true);
% svmModel=svmtrain(B,C);
% for i = 1:15
%     
%     predict(i) = svmpredict(0,D(i,:),svmModel);
% end


% Logistic regression(�޿�^�k)
% fprintf('CPU time = %g sec\n', toc);
% gC=gpuArray(single(C));		% Put C to GPU's memory
% gB=gpuArray(single(B));		% Put C to GPU's memory
% gD=gpuArray(single(D));
% [o1, o2] = arrayfun(@xycrull, gt) 
% gE = arrayfun(@mnrfit(gC,gB));

% % CPU Logistic regression(�޿�^�k)
% E=mnrfit(C,B);
% LR_Scores = mnrval(E, D)  % �w�����G�ǽT�v
% % gLR_S = gather(gScores);		% Put gScores to MATLAB's workspace

% %  GPU  Logistic regression(�޿�^�k)
% Xgpu = gpuArray(C);
% Tgpu = gpuArray(B);
% Kgpu = gpuArray(D);
% E=mnrfit(Xgpu,Tgpu);
% LR_Scores = mnrval(E,Kgpu)  % �w�����G�ǽT�v


% Neural Network(�����g����)
C1=C.';
s = length(B) ;
B3 = zeros( s , 14  ) ;
for i = 1 : s 
   B3( i , B( i )  ) = 1 ;
end

B1=B3.';


%%  To Use GPU Calculation   %%
G_devi_count = gpuDeviceCount   % ���X�i GPU�d
g = gpuDevice                     % GPU�d�����T��
D1=D.';

% [C1,B1] = vinyl_dataset;
% Xgpu = gpuArray(single(C1));
% Tgpu = gpuArray(single(B1));

% Xgpu = gpuArray(C1);
% Tgpu = gpuArray(B1);

tic
% Deep Learning 4 Hidden layers %
net = feedforwardnet([30 60 240 60 15],'trainscg');     % R=0.99164   % trainscg, traingda[30 60 240 60 15]��trainscg�ĪG�n��
% net = feedforwardnet([15 120 240 120 15]);            % traingda:�ǲ߲v�O�۰ʥi�ܪ�
% net = feedforwardnet([15 120 240 500 240 120 15]);


% MLP 1 Hidden layers %
% net = feedforwardnet(100,'trainscg');           %trainscg, traingda, traingdm

net.trainparam.show =50 ;
net.trainparam.epochs = 50000;         % Epochs:�|�a����
net.trainparam.goal = 0.001 ;
net.trainParam.lr = 0.001 ;            % �ǲ߲v:�U�p���ĳt�׺C�A���ĪGí�w�F�P�z�h�Ϥ�
net.trainParam.max_fail = 100;         % Validation checks: ���Ҧ��ơA���Ʀh�AEpochs�|�]�U�h��
% nnModel=train(net,Xgpu,Tgpu,'UseParallel','yes','UseGPU','only')  %B1= Target
nnModel=train(net,C1,B1,'UseParallel','yes','UseGPU','only')
y2 = nnModel(D1);
y2 = gather(y2);                       % �N y2�bGPU�⧹���� �Ǧ^ MATLAB's(CPU���x) workspace
G_NN_y2=y2'
fprintf('GPU time = %g sec\n', toc);


% %%  �ϥιq�������� CPU ���B��  %%
% D1=D.';
% % net = feedforwardnet(100,'traingda');                % feedforwardnet,cascadeforwardnet,timedelaynet   %%trainscg, traingda, traingdm
% net = feedforwardnet([30 60 240 60 15],'traingda'); 
% net.trainparam.show = 50 ;
% net.trainparam.epochs = 10000 ;
% net.trainparam.goal = 0.01 ;
% net.trainParam.lr = 0.001 ;
% net.trainParam.max_fail = 100;   % Validation checks
% nnModel=train(net,C1,B1);
% y2=nnModel(D1);
% C_NN_y2=y2'  % �w�����G�ǽT�v


TotalTime = etime(clock, t0)               % �p��үӶO���`�ɶ�