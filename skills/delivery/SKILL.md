---
name: delivery
description: "Özellik işlerini Agile iş kaydıyla yürütür: hazırlık ölçütü, rol sırası, bitti tanımı. Baş Mimar özellik işine başlarken kullanır."
---
# Teslimat düzeni

Her özellik için `docs/agile/stories/NNN-kisa-ad.md` dosyası aç. Roller sohbeti değil bu dosyayı okur; böylece her rol işi eksiksiz bağlamla alır.

## İş kaydı
- **Hedef:** Kim, ne istiyor, neden
- **Kabul ölçütleri:** Test edilebilir maddeler
- **Mimari kararlar:** İlgili ADR ve çizim bağlantıları
- **Etkilenenler:** Servisler, Kafka topic'leri, veri, OpenShift kaynakları
- **Görevler:** Rol, iş, durum
- **Sonuçlar:** Her rolün kısa çıktısı ve kanıtı

## Başlamaya hazır
Hedef ve kabul ölçütleri açık, etkilenenler belli, gereken mimari onaylanmış.

## Rol sırası
1. Baş Mimar kapsamı ve kararları yazar, onay alır.
2. `solution-designer` sözleşmeleri ve şemaları çıkarır.
3. Kafka'ya dokunuyorsa `kafka-expert` kodlamadan önce inceler.
4. `java-developer` kodlar ve doğrulama betiğini çalıştırır.
5. `qa-tester` kabul ölçütlerini test eder.
6. Canlıya çıkacaksa `ops-engineer` dağıtım ve geri alma planını inceler.

Küçük hatada 1-3 atlanır. Hata çıkarsa iş bir önceki role, kanıtıyla döner; aynı hata iki kez dönerse Baş Mimar bana sorar.

## Bitti tanımı
- Her kabul ölçütünün karşılığı olan bir test geçiyor
- Derleme ve testlerin gerçek çıktısı kayıtta
- Kafka değişikliği uzman onayından geçti
- Canlıya çıkacak işin geri alma planı var
- Mimari değiştiyse ADR ve çizim güncel
- Açık riskler yazılı
