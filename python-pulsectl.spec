%global pypi_name pulsectl

Name:           python-%{pypi_name}
Version:        20.1.2
Release:        1%{?dist}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio

License:        MIT
URL:            https://pypi.org/project/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/1a/a9/cdd1a19889f78ddd45775b9830045df2b4eb25f63911a2ddc3aaf8ec614f/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pulseaudio-libs

%description
Python (3.x and 2.x) high-level interface and ctypes-based bindings
for PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).


%package     -n python3-%{pypi_name}
Summary:        Python high-level interface and ctypes-based bindings for PulseAudio

%description -n python3-%{pypi_name}
Python 3.x high-level interface and ctypes-based bindings for
PulseAudio, mostly focused on mixer-like controls and
introspection-related operations (as opposed to e.g. submitting sound
samples to play, player-like client).


%prep
%setup -n %{pypi_name}-%{version}


%build
%{py3_build}


%install
%{py3_install}


%files -n python3-%{pypi_name}
%license COPYING
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*egg-info/


%changelog
* Sat Jan 25 2020 Paul W. Frields <stickster@gmail.com> - 20.1.2-1
- Update to latest upstream 20.1.2
- Testing packit

* Sat Nov  9 2019 Paul W. Frields <stickster@gmail.com> - 19.10.4-1
- Update to latest upstream 19.10.4 (#1759622)

* Mon Oct 14 2019 Paul W. Frields <stickster@gmail.com> - 19.10.0-1
- Update to latest upstream 19.10.0 (#1759622)

* Wed Sep 25 2019 Paul W. Frields <stickster@gmail.com> - 19.9.5-1
- Update to latest upstream 19.9.5 (#1754263)

* Wed Sep  4 2019 Paul W. Frields <stickster@gmail.com> - 18.12.5-1
- Initial RPM release
