#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-testit
Version  : 0.13
Release  : 89
URL      : https://cran.r-project.org/src/contrib/testit_0.13.tar.gz
Source0  : https://cran.r-project.org/src/contrib/testit_0.13.tar.gz
Summary  : A Simple Package for Testing R Packages
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
BuildRequires : buildreq-R

%description
facilitate testing R packages.

%prep
%setup -q -c -n testit
cd %{_builddir}/testit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641136385

%install
export SOURCE_DATE_EPOCH=1641136385
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library testit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library testit
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library testit
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc testit || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/testit/DESCRIPTION
/usr/lib64/R/library/testit/INDEX
/usr/lib64/R/library/testit/Meta/Rd.rds
/usr/lib64/R/library/testit/Meta/features.rds
/usr/lib64/R/library/testit/Meta/hsearch.rds
/usr/lib64/R/library/testit/Meta/links.rds
/usr/lib64/R/library/testit/Meta/nsInfo.rds
/usr/lib64/R/library/testit/Meta/package.rds
/usr/lib64/R/library/testit/NAMESPACE
/usr/lib64/R/library/testit/NEWS.Rd
/usr/lib64/R/library/testit/R/testit
/usr/lib64/R/library/testit/R/testit.rdb
/usr/lib64/R/library/testit/R/testit.rdx
/usr/lib64/R/library/testit/help/AnIndex
/usr/lib64/R/library/testit/help/aliases.rds
/usr/lib64/R/library/testit/help/paths.rds
/usr/lib64/R/library/testit/help/testit.rdb
/usr/lib64/R/library/testit/help/testit.rdx
/usr/lib64/R/library/testit/html/00Index.html
/usr/lib64/R/library/testit/html/R.css
/usr/lib64/R/library/testit/rstudio/addins.dcf
/usr/lib64/R/library/testit/tests/test-all.R
/usr/lib64/R/library/testit/tests/test-error/test-error.R
/usr/lib64/R/library/testit/tests/testit/test-assert.R
/usr/lib64/R/library/testit/tests/testit/test-utils.R
