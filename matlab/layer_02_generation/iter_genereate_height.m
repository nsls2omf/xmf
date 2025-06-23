function z2d = iter_genereate_height(standard_height_function_handle, x2d, y2d, p, q, theta, tf, z2d_measured, thr_rms_dxy)


if nargin < 8
    z2d_measured = zeros(size(x2d));
end

if nargin < 9
    thr_rms_dxy = 1e-9;
end


% Initialization
z2d = z2d_measured;
rms_dxy = Inf;

% Use while loop to make sure the transformation makes sense as
% (x2d_s, y2d_s, z2d_s) --- tf ---> (x2d, y2d, z2d) and
% (x2d, y2d, z2d) --- tf^{-1} ---> (x2d_s, y2d_s, z2d_s)
while rms_dxy > thr_rms_dxy

    % Points in metrology coordinates
    m = [x2d(:)'; y2d(:)'; z2d(:)'; ones(size(z2d(:)'))];
    % Transform back to standard mirror coordinates
    m_s = tf\m; % X_m = tansform * X_s;

    % Use standard function to generate shape in standard mirror coordinates
    x2d_s = reshape(m_s(1,:), size(x2d));
    y2d_s = reshape(m_s(2,:), size(y2d));

    try
        z2d_s = real(standard_height_function_handle(x2d_s, y2d_s, p, q, theta)); % 2D curved shape
    catch me
        if strcmp(me.identifier, 'MATLAB:TooManyInputs')
            z2d_s = real(standard_height_function_handle(x2d_s, p, q, theta)); % 1D or 2D cylinder
        else
            rethrow(me); % Rethrow error if it's not the expected one
        end
    end

    s = [x2d_s(:)'; y2d_s(:)'; z2d_s(:)'; ones(size(z2d_s(:)'))];

    % Transform to metrology coodinates to update the shape
    s_m = tf*s; % X_m = tansform * X_s;
    x2d_s_in_m = reshape(s_m(1,:), size(x2d));
    y2d_s_in_m = reshape(s_m(2,:), size(y2d));
    z2d = reshape(s_m(3,:), size(z2d));

    % Check and update the distances in lateral coordiantes
    dx2d = x2d - x2d_s_in_m;
    dy2d = y2d - y2d_s_in_m;
    rms_dxy = rms(sqrt(dx2d(:).^2 + dy2d(:).^2), 1, 'omitnan');

end




