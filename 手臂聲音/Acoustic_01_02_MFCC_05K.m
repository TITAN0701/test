clc
clear all
close all

load 'U_Run_05K_01.txt';
DATATEXT_N=U_Run_05K_01;
%%clear DATATEXT;
test_length=300000;
figure(1),subplot(3,1,1),plot(DATATEXT_N(1:150000,2),'r'),title('A01');  % MIC. sensor
axis([-inf inf -1.5 1.5]);
% figure(1),subplot(2,1,1),plot(DATATEXT_N(1:150000,1).*0.0003051850947,'r'),title('Normal');  % MIC. sensor
load 'U_Run_05K_02.txt';
DATATEXT_Y=U_Run_05K_02;
figure(1),subplot(3,1,2),plot(DATATEXT_Y(1:150000,2),'b'),title('A02');  % MIC. sensor
axis([-inf inf -1.5 1.5]);
load 'U_Run_05K_03.txt';
DATATEXT_YY=U_Run_05K_03;
figure(1),subplot(3,1,3),plot(DATATEXT_YY(1:150000,2),'g'),title('A03');  % MIC. sensor
axis([-inf inf -1.5 1.5]);


a=0.96;     %%% a==0.9~1.0
fs = 5000;
nbits = 24;

y = DATATEXT_N(1:150000,2);
yy_1 = filter([1, -a], 1, y);  %%% Filtering
time=(1:length(y))'/fs;
%wavwrite(yy_1, fs, nbits, 'A01.wav'); 

y2 = DATATEXT_Y(1:150000,2);
yy_2 = filter([1, -a], 1, y2);  %%% Filtering
time2=(1:length(y2))'/fs;
%wavwrite(yy_2, fs, nbits, 'A02.wav'); 

y22 = DATATEXT_YY(1:150000,2);
yy_22 = filter([1, -a], 1, y22);  %%% Filtering
time22=(1:length(y22))'/fs;
%wavwrite(yy_22, fs, nbits, 'A03.wav'); 

figure(2),subplot(3,1,1),
plot(time, yy_1,'r');   %%%---------Âoªi
title('Filtering-A01');
figure(2),subplot(3,1,2),
plot(time2, yy_2,'b');  %%%----------Âoªi
title('Filtering-A02');
figure(2),subplot(3,1,3),
plot(time22, yy_22,'g');  %%%----------Âoªi
title('Filtering-A03');

subplot(3,1,1);
set(gca, 'unit', 'pixel');
axisPos=get(gca, 'position');
uicontrol('string', 'Play', 'position', [axisPos(1:2), 60, 20], 'callback', 'sound(yy_1, fs)');
subplot(3,1,2);
set(gca, 'unit', 'pixel');
axisPos=get(gca, 'position');
uicontrol('string', 'Play', 'position', [axisPos(1:2), 60, 20], 'callback', 'sound(yy_2, fs)');
subplot(3,1,3);
set(gca, 'unit', 'pixel');
axisPos=get(gca, 'position');
uicontrol('string', 'Play', 'position', [axisPos(1:2), 60, 20], 'callback', 'sound(yy_22, fs)');


%%% A01 %%%
windowed_yy1=yy_1(:,1).*hamming(length(time));
[mag1, phase1, freq1]=fftOneSide(windowed_yy1, fs);

%%% A02 %%%
windowed_yy2=yy_2(:,1).*hamming(length(time2));
[mag2, phase2, freq2]=fftOneSide(windowed_yy2, fs);

%%% A03 %%%
windowed_yy22=yy_22(:,1).*hamming(length(time22));
[mag5, phase5, freq5]=fftOneSide(windowed_yy22, fs);


figure(3),
plot(freq1(1,1:75001), 20*log10(mag1(1:75001,1)),'r'); hold on
plot(freq2(1,1:75001), 20*log10(mag2(1:75001,1)),'b');
plot(freq5(1,1:75001), 20*log10(mag5(1:75001,1)),'k');
axis([-inf inf 0 50]); title('Energy spectrum (dB)'); xlabel('Frequency'); ylabel('Magnitude');
legend A01 A02 A03

% f3=freq3(:);
% fid = fopen('f3.txt', 'w');
% for i=1:301
%    fprintf(fid,'%12.8f\n', f3(i));
% end 
% fclose(fid);
% 
% m3=mag3(:);
% fid = fopen('m3.txt', 'w');
% for i=1:301
%    fprintf(fid,'%12.8f\n', m3(i));
% end 
% fclose(fid);

% f3=freq3(:);
% fid = fopen('f5.txt', 'w');
% for i=1:301
%    fprintf(fid,'%12.8f\n', f3(i));
% end 
% fclose(fid);
% 
% m3=mag3(:);
% fid = fopen('m5.txt', 'w');
% for i=1:301
%    fprintf(fid,'%12.8f\n', m3(i));
% end 
% fclose(fid);

freq3=decimate(freq1,25);
mag3=decimate(mag1,25);

freq4=decimate(freq2,25);
mag4=decimate(mag2,25);


freq6=decimate(freq5,25);
mag6=decimate(mag5,25);


% figure(3),
% subplot(2,2,1); plot(time, windowed_yy1,'r');  title('Vibration weighting'); xlabel('Time'); ylabel('Magnitude');
% subplot(2,2,2); plot(time2, windowed_yy2);  title('Acoustic weighting'); xlabel('Time'); ylabel('Magnitude');
% subplot(2,2,3); plot(freq1(1,1:75001), 20*log10(mag1(1:75001,1)),'r'); axis([-inf inf -20 50]); title('Energy spectrum (dB)'); xlabel('Frequency'); ylabel('Magnitude');
% subplot(2,2,4); plot(freq2(1,1:75001), 20*log10(mag2(1:75001,1))); axis([-inf inf -20 50]); title('Energy spectrum (dB)'); xlabel('Frequency'); ylabel('Magnitude');

figure(4),
plot(freq3(1,1:1501), 20*log10(mag3(1:1501,1)),'r'); hold on
plot(freq4(1,1:1501), 20*log10(mag4(1:1501,1)),'b');
plot(freq6(1,1:1501), 20*log10(mag6(1:1501,1)),'k');
axis([-inf inf 0 50]); title('Energy spectrum (dB)'); xlabel('Frequency'); ylabel('Magnitude');
legend A01 A02 A03
