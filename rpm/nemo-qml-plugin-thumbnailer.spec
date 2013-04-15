# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       nemo-qml-plugin-thumbnailer

# >> macros
# << macros

Summary:    Thumbnail provider plugin for Nemo Mobile
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-thumbnailer
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qml-plugin-thumbnailer.yaml
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-app-0.10)
Provides:   nemo-qml-plugins-thumbnailer > 0.3.16
Obsoletes:   nemo-qml-plugins-thumbnailer <= 0.3.16

%description
%{summary}.

%package video
Summary:    Video thumbnailer provider
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Provides:   nemo-qml-plugins-gstvideo-thumbnailer > 0.3.16
Obsoletes:   nemo-qml-plugins-gstvideo-thumbnailer > 0.3.16

%description video
%{summary}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post


%files
%defattr(-,root,root,-)
%{_libdir}/qt4/imports/org/nemomobile/thumbnailer/libnemothumbnailer.so
%{_libdir}/qt4/imports/org/nemomobile/thumbnailer/qmldir
# >> files
# << files

%files video
%defattr(-,root,root,-)
%{_libdir}/qt4/imports/org/nemomobile/thumbnailer/thumbnailers/libvideothumbnailer.so
# >> files video
# << files video