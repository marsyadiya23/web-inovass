#!/bin/bash

echo "=== K3 LAB CONTENT VERIFICATION ==="
echo ""

echo "1. CHECKING FARMASI PAGE..."
echo "   - Checking for wrong 'Kedokteran' references:"
if grep -i "kedokteran\|anatomi\|patologi\|fisiologi" layanan-detail-k3-lab-pendidikan-farmasi.html | grep -v "breadcrumb" | grep -v "comment" | head -5; then
    echo "   ❌ Found Kedokteran content in Farmasi page!"
else
    echo "   ✓ No Kedokteran references found"
fi

echo ""
echo "   - Checking for correct 'Farmasi' content:"
if grep -i "farmasi\|pharmaceutical\|API\|LAF\|fume hood\|formulasi" layanan-detail-k3-lab-pendidikan-farmasi.html | head -3; then
    echo "   ✓ Found Farmasi-specific content"
else
    echo "   ❌ Missing Farmasi content!"
fi

echo ""
echo "2. CHECKING KEPERAWATAN PAGE..."
echo "   - Checking for wrong 'Kedokteran' references:"
if grep -i "kedokteran\|anatomi\|patologi\|fisiologi" layanan-detail-k3-lab-pendidikan-keperawatan.html | grep -v "breadcrumb" | grep -v "comment" | head -5; then
    echo "   ❌ Found Kedokteran content in Keperawatan page!"
else
    echo "   ✓ No Kedokteran references found"
fi

echo ""
echo "   - Checking for correct 'Keperawatan' content:"
if grep -i "keperawatan\|nursing\|needle stick\|catheter\|wound care\|injeksi" layanan-detail-k3-lab-pendidikan-keperawatan.html | head -3; then
    echo "   ✓ Found Keperawatan-specific content"
else
    echo "   ❌ Missing Keperawatan content!"
fi

echo ""
echo "3. CHECKING ONCLICK HANDLERS IN PARENT PAGE..."
if grep -c "onclick.*farmasi" layanan-detail-k3-lab-kesehatan.html > /dev/null; then
    echo "   ✓ Farmasi onclick handler found"
else
    echo "   ❌ Farmasi onclick handler missing!"
fi

if grep -c "onclick.*keperawatan" layanan-detail-k3-lab-kesehatan.html > /dev/null; then
    echo "   ✓ Keperawatan onclick handler found"
else
    echo "   ❌ Keperawatan onclick handler missing!"
fi

echo ""
echo "=== VERIFICATION COMPLETE ==="
