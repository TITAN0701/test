%  ?��SVM?�ʥi�����G��??�z
%  1�B�����ݭn�@????�utrain�A�}�B�w��???�u��???�ʡA�b?���A?�ʥu��??�A�}��1�A2?��ܡC
%  2�B�q?svmtrain�]�u��?�z2��???�^��?�A??���?����??
%  3�B�q?svmclassify��?�A���u??�Z?�o���ҫ�svm_struct�A?????�utest?���?
clear all;
close all;
clc;
train1=[0 0;2 4;3 3;3 4;4 2;4 4;4 3;5 3;6 2;7 1;2 9;3 8;4 6;4 7;5 6;5 8;6 6;7 4;8 4;10 10];                                              %???�u?
group1=[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]'; %???�u�w����?��?
                                                                            %�Otrain?��??
test=[3 2;4 8;6 5;7 6;2 5;5 2];                                                    %???�u

%??��?�ҫ�

%svmModel = svmtrain(train,group,'kernel_function','linear','showplot',true);

%��???
%classification=svmclassify(svmModel,test,'Showplot',true);
xlsFile = 'C:\Users\abc86\Desktop\���u�n��\mfcc.xlsx';
B = xlsread(xlsFile, '�u�@��2', 'B1:B72')		% Ū�X 'Sheet2' ���������

C = xlsread(xlsFile, '�u�@��2', 'C1:KQ72')
D = xlsread(xlsFile, '�u�@��5', 'B1:KP4')
predict = zeros(4);
%SVM
%svmModel1=svmtrain(C,B,'kernel_function','linear','shoplot',true);
svmModel=svmtrain(B,C)
for i = 1:4
    % �@???�Asvmpredict�Ĥ@????�K??�N�i�H
    predict(i) = svmpredict(0,D(i,:),svmMode);
end

%Logistic regression
E=mnrfit(C,B)
Scores = mnrval(E, D);

%Neural Network
C1=C.';
s = length(B) ;
B3 = zeros( s , 3  ) ;
for i = 1 : s 
   B3( i , B( i )  ) = 1 ;
end

B1=B3.';

D1=D.';
net = feedforwardnet(50);
net.trainparam.show = 50 ;
net.trainparam.epochs = 500 ;
net.trainparam.goal = 0.01 ;
net.trainParam.lr = 0.01 ;
nnModel=train(net,C1,B1)
y2=nnModel(D1)
y2=y2'