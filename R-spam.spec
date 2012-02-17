%bcond_without bootstrap
%global packname  spam
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.28_0
Release:          1
Summary:          SPArse Matrix
Group:            Sciences/Mathematics
License:          GPL | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.28-0.tar.gz
Requires:         R-methods 
%if %{with bootstrap}
Requires:         R-SparseM R-Matrix 
%else
Requires:         R-fields R-SparseM R-Matrix 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
%if %{with bootstrap}
BuildRequires:    R-SparseM R-Matrix 
%else
BuildRequires:    R-fields R-SparseM R-Matrix 
%endif

%description
Set of function for sparse matrix algebra.  Differences with
SparseM/Matrix are: (1) we only support (essentially) one sparse matrix
format, (2) based on transparent and simple structure(s), (3) tailored for
MCMC calculations within GMRF. (4) S3 and S4 like-"compatible" ...  and it
is fast.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/0NEWS
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/demodata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
