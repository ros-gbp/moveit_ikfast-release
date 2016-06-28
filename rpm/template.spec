Name:           ros-indigo-moveit-ikfast
Version:        3.1.1
Release:        0%{?dist}
Summary:        ROS moveit_ikfast package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org/wiki/Kinematics/IKFast
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin

%description
Generates a IKFast kinematics plugin for MoveIt using OpenRave generated cpp
files.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jun 28 2016 G.A. vd. Hoorn <g.a.vanderhoorn@tudelft.nl> - 3.1.1-0
- Autogenerated by Bloom

* Tue Oct 07 2014 G.A. vd. Hoorn <g.a.vanderhoorn@tudelft.nl> - 3.1.0-0
- Autogenerated by Bloom

* Tue Oct 07 2014 Dave Coleman <davetcoleman@gmail.com> - 3.0.7-1
- Autogenerated by Bloom

